#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 任务，在python中重构读取弹幕的代码。
# 主函数，支持被代码guitest.py作为次级进程打开，独立运行时如果不想使用默认设置，请以命令行形式添加输入参数
# import json
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
    parser.add_option('-w', '--word', dest='target', default='kksk', help='查询关键字')
    parser.add_option('-l', '--limit', dest='limit', default=14, help='纳入统计的最小阈值')
    parser.add_option('-v', '--interval', dest='interval', default=20, help='统计最小间隔')
    parser.add_option('-g', '--group', dest='group', default=5, help='从当前时间轴开始向前读group秒，若达到limit，则将结果记录，并跳过interval秒')
    parser.add_option('-f', '--flag', dest='flag', default=0, help='被gui调用时的标志，此时回传scale和秒制时间')
    parser.add_option('-d', '--download', dest='task_type', default=0, help='如果是从已存在的B站视频中读入轴进行分析，是否顺带保存到本地')
    (options, args) = parser.parse_args()
    return options


def match_target_word(line: str, target: str) -> int:
    """
    判断字符串是否包含所需内容
    :param line:
    :param target:
    :return:
    """
    # line = line.strip()#预处理
    # line = line.replace('\n','')#预处理
    target = target.replace('(', r'\(')  # 预处理
    target = target.replace(')', r'\)')  # 预处理
    target = target.replace(r"'", r'&apos')  # 预防出错
    if re.search(target, re.sub(r'<(.*?)>', '', strQ2B(line)), re.I):  # 对于弹幕内容不分大小写地进行匹配，若匹配成功则执行
        time = re.search(r'"(.*?),', line).group(1)  # 正则查找语句, 非贪婪匹配，尝试匹配第一个冒号和第一个逗号之间的内容，即时间
        return int(float(time))  # 字符串转数字
    else:
        return 0


def count_frequency(counts, scale) -> list:
    """
    读取数组，进行统计
    :param counts:
    :param scale:
    :return:
    """
    frequency = [0 for _ in range(scale + 1)]  # 创建一个scale+1大小的数组，其中包括0~scale
    for count in counts:
        frequency[count] += 1
    return frequency


def sec2time(sec):
    """
    将秒制时间转换成时间时分秒
    :param sec:
    :return:
    """
    h = int(sec) // 3600
    m = int(sec) // 60 % 60
    s = sec % 60
    # f = int(sec * 1000) % 1000
    return "%02d:%02d:%02d" % (h, m, s)


def analyse_and_dump(frequency, output_file, limit, interval=20, group=5, flag=0):
    """
    对弹幕文件执行分析, 弹幕统计方法改为时间复杂度低的滑动窗口，sum(frequency[index:index+group-1])代码可能引起bug，需要留意
    :param frequency: 弹幕出现频度
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
                    print(str(sec2time(index)) + ": " + str(count), file=f)  # 写入文件
                    print(str(sec2time(index)) + ": " + str(count))  # 输出到控制台，便于调试
                    index += interval  # 若记录了一次，跳过一段时间再重新开始判定是否可以记录
                    if index > (len(frequency) - group + 1):
                        break
                    for _ in range(interval - 1):  # 迭代器跳过一定迭代次数
                        next(indexes, None)
                    count = sum(frequency[index:index + group - 1])
                else:
                    count -= frequency[index]
            print("描述信息： ", file=f)  # 写入文件
            print("     阈值(limit)：" + str(args.limit), file=f)  # 写入文件
            print("     关键词(word)：" + str(args.target), file=f)  # 写入文件
            print("     冷却间隔(interval)：" + str(args.interval), file=f)  # 写入文件
            print("     统计区间长度(interval)：" + str(args.group), file=f)  # 写入文件
    except IndexError:
        print('Error: analyse_function error, 数组越界' + '\n一般这种情况是我敲错了')
        exit(1)
    except IOError:
        print('Error: 读写错误')
        exit(1)


def get_dan_mu(vid: str):
    """
    获取弹幕xml，支持读取特定分P的结果
    :param vid:
    :return:
    """
    tmp = vid.split(',')
    vid = tmp[0]
    if vid.startswith("BV"):
        resp = requests.get(f"{BILIBILI_API_PAGELIST_BVID}{vid}")
    elif vid.startswith("av"):
        resp = requests.get(f"{BILIBILI_API_PAGELIST_AVID}{vid[2:]}")
    elif vid.isdigit():
        resp = requests.get(f"{BILIBILI_API_PAGELIST_AVID}{vid}")
    else:
        return None
    if resp.ok:
        if len(tmp) == 1:
            cid = resp.json()["data"][0]["cid"]
        elif len(tmp) == 2:
            page = int(tmp[1]) - 1
            if page < 0:
                raise ValueError("不合法的分页")
            cid = resp.json()["data"][int(tmp[1]) - 1]["cid"]
        else:
            raise ValueError("不合法的逗号数量")
        return requests.get(f"{BILIBILI_API_DANMU_LIST}{cid}")
    else:
        return None


def strQ2B(text: str) -> str:
    """
    全角字符转换成半角字符
    :param text:
    :return:
    """
    tmp = []
    for word in text:
        code = ord(word)
        if code == 12288:  # 转换空格
            code = 32
        elif 65281 <= code <= 65374:  # 转换字符、数字及字母
            code -= 65248
        tmp.append(chr(code))
    return "".join(tmp)  # 由append和for循环产生的是一个list，经过join后成为字符串。另外，双引号中的内容规定了拼接时使用何种连接符


def process_online_video(vid, counts):
    """
    处理在线视频
    :param vid:
    :param counts:
    :return:
    """
    max_time_scale: int = 0
    original_xml = get_dan_mu(vid)
    if args.task_type:
        """
        是否下载
        """
        pretty_xml = xml.dom.minidom.parseString(original_xml.content).toprettyxml()
        try:
            with open(vid + '.xml', 'w', encoding='UTF-8') as f:
                for line in pretty_xml.splitlines():
                    f.write(line)
                    if line == '</i>':
                        break
                    else:
                        tempt = match_target_word(line, args.target)  # 寄存返回值
                        if tempt:
                            max_time_scale = max(max_time_scale, tempt)
                            counts.append(tempt)
                    f.write('\n')
        except IOError:
            print('Error:cant read the xml file' + '\n一般这种情况下是你敲错了文件名')
            exit(1)
    else:
        root = ET.fromstring(original_xml.content)
        for danmu in root.findall("d"):
            if re.search(
                    args.target.replace("?", r"\?"),  # ?为regex关键字，需要加"\"进行转义
                    strQ2B(danmu.text),  # 把全角符号、数字及字母转换为半角
                    re.I,  # 忽略大小写
            ):
                sec = math.floor(float(danmu.attrib["p"].split(",")[0]))  # 获取弹幕时间
                counts.append(sec)  # 该数组用于记录
                max_time_scale = max(max_time_scale, sec)  # 记录最后一条弹幕时间

    return max_time_scale


def process_local_xml(counts):
    """
    处理本地xml文件
    :param counts:
    :return:
    """
    max_time_scale: int = 0
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
        print('Error:数组越界' + '\n一般这种情况下是我逻辑敲错了')
        exit(1)
    except IOError:
        print('Error:cant read the xml file' + '\n一般这种情况下是你敲错了文件名')
        exit(1)

    return max_time_scale


if __name__ == '__main__':
    args = get_args()  # 调用以获取文件信息
    counts = []  # 初始化数组, 该数组用于记录匹配弹幕出现的时间
    if args.xml_file.startswith("BV") or args.xml_file.startswith("av"):
        """
        说明此时不是xml文件，是视频号
        """
        max_time_scale = process_online_video(args.xml_file, counts)

    else:
        """
        说明此时是xml文件，这里默认文件自带换行
        """
        args.xml_file = re.sub(r'\..*', '', args.xml_file) + '.xml'  # 校正文件后缀，容错
        max_time_scale = process_local_xml(counts)

    if args.flag:  # 用于给guitest.py提供（有效的）进度条总长
        print(max_time_scale)

    if args.out_file == '':  # 若未定义输出文件名称，则复制输入名称
        args.out_file = args.xml_file

    args.out_file = re.sub(r'\..*', '', args.out_file) + '.txt'  # 更改后缀为txt

    frequency = count_frequency(counts, max_time_scale)

    analyse_and_dump(frequency, args.out_file, int(args.limit), int(args.interval),
                     int(args.group), int(args.flag))

    # 如果要脱离gui使用，请取消注释下面的代码：
    # os.system('pause')

# 命令行使用示例
"""
    cd D:\python_code\ReadKkskFromText  # 改成切换到这个文件的真实路径 
    
    python read_kksk_from_text.py -i D:\Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 1.txt -w 草 -l 20
    
    python read_kksk_from_text.py -i D:\Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 2.txt -w kksk -l 14
    
    python read_kksk_from_text.py -i D:\Ccode\readthekkskfromtxt\readthekkskfromtxt\20190527_220250.xml -o 2.txt -w KKsk -l 12
    
    如果要在线读取：
    python read_kksk_from_text.py -i BV19t411K7Kn -o 2.txt -w KKsk -l 12
    
    如果要在线读取并下载xml文件到本地：
    python read_kksk_from_text.py -i BV19t411K7Kn -o 2.txt -w KKsk -l 12 -d 1
    
    如果有分P：
    python read_kksk_from_text.py -i BV19t411K7Kn,2 -o 2.txt -w KKsk -l 12 -d 1
    
"""
