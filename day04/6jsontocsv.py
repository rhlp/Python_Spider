# -*- coding:utf-8 -*-
# json转换csv文件

import json
import csv

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def json_to_csv():

    # 1.读取json文件
    json_file = open("5tencent.json", "r")

    # 2.创建csv文件
    csv_file = open("6json.csv", "w")

    # 3.创建读写器
    csv_writer = csv.writer(csv_file)

    # 4.提取表头和正文内容
    data = json.load(json_file)

    # 表头
    sheet_title = data[0].keys()
    # 内容
    content_list = []
    for dic in data:
        content_list.append(dic.values())

    # content_list = [dic.values() for dic in data]

    # 通过读写器 写入文件
    csv_writer.writerow(sheet_title)
    csv_writer.writerows(content_list)

    # 关闭文件
    json_file.close()
    csv_file.close()

if __name__ == '__main__':
    json_to_csv()