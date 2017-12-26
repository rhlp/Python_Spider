# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time

class douyu_spider():
    def __init__(self):
        self.base_url = "https://www.douyu.com/directory/all"
        self.count = 0
        self.driver = webdriver.PhantomJS()

    def send_request(self):
        time.sleep(1)
        self.driver.get(self.base_url)
        data = self.driver.page_source
        return data

    def analysis_data(self, data):
        # 1.转换类型
        soup = BeautifulSoup(data, "lxml")

        # 2.选择器解析

        # 2.1房间的名字
        home_list = soup.select('#live-list-content .ellipsis')

        # 2.2主播的名字
        name_list = soup.select('#live-list-content .dy-name')

        # 2.3人气
        super_list = soup.select('#live-list-content .dy-num')

        # 3.发内容拼接 打印显示
        for home, name, supers in zip(home_list, name_list, super_list):
            print home.get_text().strip()
            print name.get_text()
            print supers.get_text()
            self.count += 1

        print self.count



if __name__ == '__main__':
    tool = douyu_spider()
    data = tool.send_request()
    tool.analysis_data(data)

