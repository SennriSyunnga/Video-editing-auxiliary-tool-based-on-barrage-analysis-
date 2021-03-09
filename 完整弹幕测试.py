#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import re
import requests  # 第三方库，通过pip安装
import xml.etree.ElementTree as ET


from datetime import timedelta

import matplotlib.pyplot as plt  # 第三方库，通过pip安装
from matplotlib.ticker import FuncFormatter, StrMethodFormatter  # 第三方库，通过pip安装

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用支持显示中文及日文字符的字体

BILIBILI_API = "https://api.bilibili.com/x"
BILIBILI_API_PAGELIST_AVID = f"{BILIBILI_API}/player/pagelist?aid="
BILIBILI_API_PAGELIST_BVID = f"{BILIBILI_API}/player/pagelist?bvid="
BILIBILI_API_DANMU_LIST = f"{BILIBILI_API}/v1/dm/list.so?oid="


def timeformatter(y, pos):  # 格式化柱形图时间
    return str(timedelta(seconds=math.floor(y))) if y >= 0 else "无效时间"


formatter = FuncFormatter(timeformatter)


def getDanmu(vid):  # 获取弹幕xml
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


def strQ2B(text):  # 全角字符转换成半角字符
    tmp = []
    for word in text:
        code = ord(word)
        if code == 12288:  # 转换空格
            code = 32
        elif 65281 <= code <= 65374:  # 转换字符、数字及字母
            code -= 65248
        tmp.append(chr(code))
    return "".join(tmp)  # 由append和for循环产生的是一个list，经过join后成为字符串。另外，双引号中的内容规定了拼接时使用何种连接符


keywords = "kksk|草|めあ|mea|谁|誰|??".split("|")  # 关键字
similar_words = {"めあ": "めあ/mea", "mea": "めあ/mea", "谁": "谁/誰", "誰": "谁/誰"}  # 同义词
matches = {
    similar_words[keyword] if keyword in similar_words else keyword: []
    for keyword in keywords
}
last = 0

danmuxml = getDanmu("BV1kV411v7vc")
if danmuxml and danmuxml.ok:
    root = ET.fromstring(danmuxml.content)
    for danmu in root.findall("d"):
        t = float(danmu.attrib["p"].split(",")[0])  # 获取弹幕时间
        if t > last:
            last = math.ceil(t)  # 记录最后一条弹幕时间
        for keyword in keywords:  # 关键字匹配
            if re.search(
                keyword.replace("?", r"\?"),  # ?为regex关键字，需要加"\"进行转义
                strQ2B(danmu.text),  # 把全角符号、数字及字母转换为半角
                re.I,  # 忽略大小写
            ):
                matches[
                    similar_words[keyword] if keyword in similar_words else keyword
                ].append(t)  # 这里实现了一个嵌套关系,首先如果关键词出现在同义词字典中，将几个同义词重新定向为同一语义。
                # 这里应当开启一个是否支持同义词识别的选项，以适应细分化的用户需求：如，不想识别同义词的情况。默认开启，放置在二级页面下。
    # 绘制柱形图
    fig, ax = plt.subplots()
    ax.set_xlabel("时间")
    ax.set_ylabel("个数")
    ax.set_xlim(left=0, right=last)  # 可选，设置时间轴范围从00:00:00到最后一条弹幕时间
    ax.set_ylim(bottom=8, top=32)  # 可选，设置次数的上下限
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(StrMethodFormatter("{x:.0f}"))
    plt.hist(  # 绘制柱形图
        matches.values(),  # 以时间频率为纵坐标
        label=matches.keys(),  # 以关键字为横坐标
        bins=256,  # bins指定出现的柱形个数
    )
    plt.legend()
    ax.set_title("关键弹幕次数统计")
    plt.show()
else:
    print("无法获取弹幕xml")