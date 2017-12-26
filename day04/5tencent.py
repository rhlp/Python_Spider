# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import requests
import json
import time


class tencent_job(object):
    def __init__(self):
        self.base_url = "http://hr.tencent.com/position.php?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.item_list = []
    # 发送请求
    def send_request(self, url, params={}):
        time.sleep(1)
        try:
            response = requests.get(url, params=params, headers=self.headers).content
            return response
        except Exception, err:
            print err

    # 解析数据
    def analysis_data(self, data):

        # 1.转换类型
        soup = BeautifulSoup(data, "lxml")

        # 2.获取标签
        data_list = soup.select(".even,.odd")

        # 将里面的每一行的数据 提取出来
        for tr in data_list:
            dict = {}
            dict["work_name"] = tr.select("td a")[0].get_text()
            dict["work_type"] = tr.select("td")[1].get_text()
            dict["work_count"] = tr.select("td")[2].get_text()
            dict["work_place"] = tr.select("td")[3].get_text()
            dict["work_time"] = tr.select("td")[4].get_text()
            self.item_list.append(dict)

    # 写入本地文件
    def write_file(self):
        # 将列表转换成字符串 str
        data_str = json.dumps(self.item_list)
        with open("5tencent.json", "w") as f:
            f.write(data_str)

    def start_work(self):
        for page in range(0, 80, 10):
            print page
            # 1.拼接参数
            params = {
                "keywords": "python",
                "lid": "2156",
                "tid": "87",
                "start": "0",
            }
            # 2.发送请求
            data = self.send_request(self.base_url, params=params)

            # 3.解析数据
            self.analysis_data(data)

        # 写入文件
        self.write_file()

if __name__ == '__main__':
    tool = tencent_job()
    tool.start_work()

    # 发送请求

    # 解析数据

    # 写入本地

    # 调度方法