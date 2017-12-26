# -*- coding:utf-8 -*-

import requests
import random
import jsonpath
import json
import time


class lagou_spider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json"
        self.headers = {
            # "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "zh-CN,zh;q=0.9",
            # "Connection": "keep-alive",
            # 反爬字段1
            "Cookie": "user_trace_token=20171201231943-0ebc06e9-d6ab-11e7-9b7b-5254005c3644; LGUID=20171201231943-0ebc0e26-d6ab-11e7-9b7b-5254005c3644; _ga=GA1.2.601932588.1512141581; JSESSIONID=ABAAABAAADEAAFI775017F0645632F663D5DFA52E717C66; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512141581,1514009751; TG-TRACK-CODE=index_search; index_location_city=%E5%8C%97%E4%BA%AC; LGSID=20171223215719-30f682c8-e7e9-11e7-a76c-525400f775ce; _gat=1; SEARCH_ID=863cbdf835b84b91a76888b21d206060; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514039289; LGRID=20171223222808-7f38dadb-e7ed-11e7-a770-525400f775ce",
            # "Host": "www.lagou.com",
            # 反爬字段2
            "Referer": "https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            # "X-Anit-Forge-Code": "0",
            # "X-Anit-Forge-Token": "None",
            # "X-Requested-With": "XMLHttpRequest",
        }

        self.search_name = raw_input("请输入搜索专业:")
        self.city = raw_input("请输入城市名字：")

        self.page = 1
        self.proxy_list = [
            {"http": "mr_mao_hacker:sffqry9r@120.27.218.32:16816"},
            {}
        ]
        self.item_list = []
        self.iswork = True

    # 请求数据
    def send_request(self):
        print "正在抓取第%d" % self.page
        time.sleep(1)

        # 1.params
        params = {
            "px": "default",
            "city": self.city,
            "needAddtionalResult": "false",
            "isSchoolJob": "0"
        }

        # 2.data
        formdata = {
            "first": "false",
            "pn": self.page,
            "kd": self.search_name
        }

        # 3.随机获取代理
        random_proxy = random.choice(self.proxy_list)
        try:
            response = requests.post(self.base_url, params=params, data=formdata, headers=self.headers)
            data = response.json()
            return data
        except Exception, err:
            print err

    # 解析数据
    def analysis_data(self, data):
        # 1.取出职位信息
        result_data = jsonpath.jsonpath(data, "$..result")[0]
        print len(result_data)

        if not len(result_data):
            print "数据爬取结束！！！"
            self.iswork = False
            return

        # 2.循环取出 字典数据 二次解析
        for content in result_data:
            dict = {}
            dict["positionName"] = content["positionName"]
            dict["salary"] = content["salary"]
            dict["education"] = content["education"]
            self.item_list.append(dict)

    # 写入本地
    def write_file(self, data):
        print "数据保存成功..."
        json.dump(self.item_list, open("2lagou2_pyth.json", "w"))

    # 调度的方法
    def start_work(self):
        while self.iswork:
            data = self.send_request()
            self.analysis_data(data)
            self.page += 1
        self.write_file(data)

if __name__ == '__main__':
    tool = lagou_spider()
    tool.start_work()

