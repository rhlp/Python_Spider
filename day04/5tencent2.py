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
        self.page = 0

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

        # 3.将里面的每一行的数据 提取出来
        for tr in data_list:
            dict = {}
            dict["work_name"] = tr.select("td a")[0].get_text()
            dict["work_type"] = tr.select("td")[1].get_text()
            dict["work_count"] = tr.select("td")[2].get_text()
            dict["work_place"] = tr.select("td")[3].get_text()
            dict["work_time"] = tr.select("td")[4].get_text()
            self.item_list.append(dict)

        # 4. 返回 判断是否是最后一页 的条件: 是否有 noactive 值
        # 4.1 找到下一页的标签
        next_lable = soup.select("#next")
        # 4.2 根据标签 获取里面的class 的属性值
        # 注意:class返回的列表,前面为空,不需要去取内容
        judge = next_lable[0].get("class")

        return judge

    # 写入本地文件
    def write_file(self):
        # 将列表转换成字符串 str
        data_str = json.dumps(self.item_list)
        with open("5tencent2.json", "w") as f:
            f.write(data_str)

    def start_work(self):
        for page in range(0, 80, 10):
            # print page
            # 1.拼接参数
            params = {
                "keywords": "python",
                "lid": "2156",
                "tid": "87",
                "start": self.page,
            }
            # 2.发送请求
            data = self.send_request(self.base_url, params=params)

            # 3.解析数据  -->返回 判断是否是最后一页的条件
            judge = self.analysis_data(data)

            self.page += 10
            print self.page
            # 4.如果到了最后一页 noactive出现, 跳出循环,终止爬虫
            if judge:
                break

        # 写入文件
        self.write_file()

if __name__ == '__main__':
    tool = tencent_job()
    tool.start_work()

    # 发送请求

    # 解析数据

    # 写入本地

    # 调度方法