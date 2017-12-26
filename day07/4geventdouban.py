# -*- coding:utf-8 -*-

import requests
from lxml import etree
import time

# 导入协程
import gevent
from gevent import monkey
monkey.patch_all()


class douban_movie_data(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/top250"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.count = 0

    # 发送请求
    def send_request(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            data = response.content
            self.analysis_data(data)
        except Exception, err:
            print err

    # 解析数
    def analysis_data(self,data):

        # 1.转换类型
        html_data = etree.HTML(data)

        # 2.xpath
        name_list = html_data.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')

        # 打印查看
        for name in name_list:
            print name
            self.count += 1

    # 调度方法
    def start_work(self):
        start_time = time.time()

        url_list = []
        gevent_list = []
        for page in range(0, 225+1, 25):
            # 拼接url
            url = self.base_url + "?" + "start="+str(page)
            url_list.append(url)
            # print url_list

            # 创建协程
            gevents = gevent.spawn(self.send_request, url)
            gevent_list.append(gevents)

        # 主线程等待子线程
        gevent.joinall(gevent_list)

        end_time = time.time()
        all_time = end_time - start_time
        print "总共电影%d" % self.count
        print "总共的时间是%s" % all_time

    def sum(self,num):
        return num + 100

if __name__ == '__main__':

    tool = douban_movie_data()
    tool.start_work()
