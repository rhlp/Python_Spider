# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time

class douyu_spider():
    def __init__(self):
        self.base_url = "https://www.douyu.com/directory/all"
        self.count = 0
        self.driver = webdriver.PhantomJS()
        self.page = 1

    def send_request(self):
        self.driver.get(self.base_url)

        # 下一页的标签 class = 'shark-pager-next'
        #  什么时候结束class =  shark-pager-disable-next  如果有:结束了; 没有继续循环

        while True:
            print "正在下载的页数%d" % self.page
            time.sleep(1)
            self.page += 1
            data = self.driver.page_source
            self.analysis_data(data)

            # 获取 最后shark-pager-disable-next
            # 挂了 找不见
            # self.driver.find_element_by_class_name('shark-pager-disable-next')

            # 用字符串find查找 -1 字符串
            if data.find("shark-pager-disable-next") != -1:
                break

            # 点击下一页 继续获取数据
            self.driver.find_element_by_class_name('shark-pager-next').click()

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

