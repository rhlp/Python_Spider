# -*- coding:utf-8 -*-

import requests
import re

import time

class Neihan_spider(object):
    def __init__(self):
        self.base_url = "http://www.neihan8.com/article/list_5_"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

        # 第一层正则表达式 <div class="f18 mb20">
        # 千万注意: 正则表达式里面的符号不能改
        self.first_pattern = re.compile(r'<div class="f18 mb20">.*?</div>', re.S)

        # 第二层数据正则表达式
        # 1.所有标签无论开关 <.*?>
        # 2.字符实体 &(.*?);
        # 3.空白 \s
        # 4.全角的空格
        self.second_pattern = re.compile(r'<.*?>|&(.*?);|\s|　　')

    # 1.发送请求
    def send_request(self, url):
        time.sleep(1)
        try:
            response = requests.get(url, headers=self.headers)
            return response.content
        except Exception, err:
            print err

    # 写入本地
    def write_file(self, data, page):
        with open("4neihan4.txt", "a") as f:
            # 区分第几页的数据
            filename = "第" + str(page) + "页的段子\n"
            print filename
            f.write(filename)

            for content in data:
                # 第二层解析
                second_data = self.second_pattern.sub("", content)
                f.write(second_data)
                # 在每个段子结束的时候价格换行
                f.write("\n\n")

    # 解析数据
    def analysis_data(self, data):
        # 解析第一层数据 将每一个段子提取出来
        data_list = self.first_pattern.findall(data)

        return data_list


    # 4.调度方法
    def start_work(self):
        # 循环调用
        for page in range(1, 5):

            # 1.拼接url
            url = self.base_url + str(page) + ".html"

            # 2.发送请求
            data = self.send_request(url)

            # 转码: 原因:内涵网址的数据默认编码gbk ;
            # 所有码都和unicode 可以互转
            data =data.decode("gbk").encode("utf-8")

            # 3.解析第一层的数据
            second_data = self.analysis_data(data)

            # 将第一次解析完毕的数据写入
            self.write_file(second_data, page)


if __name__ == '__main__':

    tool = Neihan_spider()
    tool.start_work()


