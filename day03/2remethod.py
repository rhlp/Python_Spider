# -*- coding:utf-8 -*-

import re

if __name__ == '__main__':

    # 正则 在哪里都一样
    # 每种语言调用的方法不一致

    # 1.match 默认从头开始  匹配一次
    # 纯数字的正则 ^\d+$
    match_str = "abc123"
    pattern = re.compile("\d+")
    # print pattern

    # 第二个参数指定开始位置, 第三个参数指定结束的位置
    result = pattern.match(match_str, 3, 4)

    # 2.search 默认任意位置开始 匹配一次
    result = pattern.search(match_str, 1, 2)

    # 3.findall 全局 返回的是列表
    all_str = "abdsffsdbfsdsbfdsfb"
    all_pattern = re.compile(r"b")
    result = all_pattern.findall(all_str)

    # 4.finditer 全局 返回 迭代对像
    result = all_pattern.finditer(all_str)

    for page in result:
        print page.group()
