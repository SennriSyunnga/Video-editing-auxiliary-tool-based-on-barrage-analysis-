#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 任务，在python中重构读取弹幕的代码。
# 主函数，支持被代码guitest.py作为次级进程打开，独立运行时如果不想使用默认设置，请以命令行形式添加输入参数
# import json
import os
import math
import re
from optparse import OptionParser
import requests  # 第三方库，通过pip安装
import xml.dom.minidom
import xml.etree.ElementTree as ET

BILIBILI_API = "https://api.bilibili.com/x"
BILIBILI_API_PAGELIST_AVID = f"{BILIBILI_API}/player/pagelist?aid="
BILIBILI_API_PAGELIST_BVID = f"{BILIBILI_API}/player/pagelist?bvid="
BILIBILI_API_DANMU_LIST = f"{BILIBILI_API}/v1/dm/list.so?oid="


def get_args():
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='xml_file', default='danmu.xml', help='输入文件名，可包含后缀和指定路径')
    parser.add_option('-o', '--output', dest='out_file', default='', help='输出文件名，可包含后缀和指定路径')
    # parser.add_option('-t', '--type', dest='type', default='srt', help='')
    parser.add_option('-w', '--word', dest='target', default='kksk', help='查询关键字')
    parser.add_option('-l', '--limit', dest='limit', default=14, help='纳入统计的最小阈值')
    parser.add_option('-v', '--interval', dest='interval', default=20, help='统计最小间隔')
    parser.add_option('-g', '--group', dest='group', default=5, help='从当前时间轴开始向前读group秒，若达到limit，则将结果记录，并跳过interval秒')
    parser.add_option('-f', '--flag', dest='flag', default=0, help='被gui调用时的标志，此时回传scale和秒制时间')
    (options, args) = parser.parse_args()
    return options


def match_target_word(line, target):  # 判断字符串是否包含所需内容
    # line = line.strip()#预处理
    # line = line.replace('\n','')#预处理
    target = target.replace('(', r'\(')  # 预处理
    target = target.replace(')', r'\)')  # 预处理
    target = target.replace(r"'", r'&apos')  # 预防出错
    if re.search(target, re.sub(r'<(.*?)>', '', line), re.I):  # 对于弹幕内容不分大小写地进行匹配，若匹配成功则执行：
        # print(line.encode('gbk','ignore').decode('gbk'))
        time = re.search(r'"(.*?),', line).group(1)  # 正则查找语句
        return int(float(time))  # 字符串转数字
    else:
        return None


def count_frequency(counts, scale):  # 读取数组，进行统计
    frequency = [0 for _ in range(scale + 1)]  # 创建一个scale+1大小的数组，其中包括0~scale
    for count in counts:
        frequency[count] += 1
    return frequency


def sec2time(sec):  # 将秒制转换成时间
    h = int(sec) // 3600
    m = int(sec) // 60 % 60
    s = sec % 60
    # f = int(sec * 1000) % 1000
    return "%02d:%02d:%02d" % (h, m, s)


def analyse(frequency, output_file, limit, interval=20, group=5, flag=0):
    """
    对弹幕文件执行分析, 计算方法改为滑动窗口，sum(frequency[index:index+group-1])代码可能引起bug，需要留意
    :param frequency: 频度
    :param output_file: 对外输出文件的名字
    :param limit: 纳入统计的最低数量
    :param interval: 记轴后的冷却时间间隔
    :param group: 浓度计算区间
    :param flag: 是否当前被GUI调用
    :return:
    """
    try:
        with open(output_file, 'w') as f:
            indexes = iter(range(len(frequency) - group + 1))
            count = sum(frequency[0: group - 1])  # 滑动窗口
            for index in indexes:
                right = index + group - 1
                count += frequency[right]
                if count >= limit:
                    if flag:
                        print(index)
                    print(sec2time(index), file=f)  # 写入文件
                    print(sec2time(index))  # 输出到控制台
                    index += interval  # 若记录了一次，跳过一段时间再重新开始判定是否可以记录
                    if index > (len(frequency) - group + 1):
                        break
                    for _ in range(interval - 1):  # 迭代器跳过一定迭代次数
                        next(indexes, None)
                    count = sum(frequency[index:index + group - 1])
                else:
                    count -= frequency[index]
    except IndexError:
        print('Error: analyse_function error, 数组越界' + '\n一般这种情况是我敲错了')
        exit(1)


def getDanMu(vid):
    """
    获取弹幕xml, 后续集成
    :param vid:
    :return:
    """
    if vid.startswith("BV"):
        resp = requests.get(f"{BILIBILI_API_PAGELIST_BVID}{vid}")
    elif vid.startswith("av"):
        resp = requests.get(f"{BILIBILI_API_PAGELIST_AVID}{vid[2:]}")
    elif vid.isdigit():
        resp = requests.get(f"{BILIBILI_API_PAGELIST_AVID}{vid}")
    else:
        return None
    if resp.ok:
        cid = resp.json()["data"][0]["cid"]
        return requests.get(f"{BILIBILI_API_DANMU_LIST}{cid}")
    else:
        return None


if __name__ == '__main__':
    args = get_args()  # 调用以获取文件信息
    counts = []  # 初始化数组, 该数组用于记录匹配弹幕出现的时间
    max_time_scale = 0
    if args.xml_file.startswith("BV") or args.xml_file.startswith("av"):
        """
        说明此时不是xml文件，是视频号
        """
        original_xml_content = getDanMu(args.xml_file).text
        pretty_xml = xml.dom.minidom.parseString(original_xml_content).toprettyxml()
        for line in pretty_xml.splitlines():
            if line == '</i>':
                break
            else:
                tempt = match_target_word(line, args.target)  # 寄存返回值
                if tempt:
                    max_time_scale = max(max_time_scale, int(float(tempt)))
                    counts.append(tempt)  # 该数组用于记录
    else:
        """
        说明此时是xml文件
        """
        args.xml_file = re.sub(r'\..*', '', args.xml_file) + '.xml'  # 校正文件后缀，容错
        try:
            for line in open(args.xml_file, 'r', encoding='UTF-8'):
                if line == '</i>':
                    break
                else:
                    tempt = match_target_word(line, args.target)  # 寄存返回值
                    if tempt:
                        max_time_scale = max(max_time_scale, int(float(tempt)))
                        counts.append(tempt)  # 该数组用于记录
        except IndexError:
            print('Error:数组越界' + '\n一般这种情况下是我敲错了')
            exit(1)
        except IOError:
            print('Error:cant read the xml file' + '\n一般这种情况下是你敲错了文件名')
            exit(1)

    if args.flag:
        print(max_time_scale)

    if args.out_file == '':  # 若未定义输出文件名称，则复制输入名称
        args.out_file = args.xml_file

    args.out_file = re.sub(r'\..*', '', args.out_file) + '.txt'  # 更改后缀为txt

    frequency = count_frequency(counts, max_time_scale)

    analyse(frequency, args.out_file, int(args.limit), int(args.interval),
            int(args.group), int(args.flag))

    # os.system('pause')

# 使用示例
"""
cd D:\python_code\ReadKkskFromText
python read_kksk_from_text.py -i /Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 1.txt -w 草 -l 20
python read_kksk_from_text.py -i /Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 2.txt -w kksk -l 14
python read_kksk_from_text.py -i D:\Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 2.txt -w KKsk -l 12
"""
