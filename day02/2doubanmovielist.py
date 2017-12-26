# -*- coding:utf-8 -*-

import urllib2
import urllib
import time

class Doubanspider(object):
    def __init__(self):
        # ajax请求: 必须通过抓包
        self.base_url = "https://movie.douban.com/j/chart/top_list?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        time.sleep(2)
        try:
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            if response.getcode() == 200:
                return response.read()

        except Exception, err:
            print err

    # 2.保存本文件
    def write_file(self, data):
        with open("2doubanhome.html", "w") as f:
            f.write(data)

    # 调度的方法
    def start_work(self):
        params = {
            "type": "5",
            "interval_id": "100:90",
            "action": "",
            "start": "0",
            "limit": "20",
        }

        # 拼接 url + params_str
        params_str = urllib.urlencode(params)
        url = self.base_url + params_str

        data = self.send_request(url)
        self.write_file(data)

if __name__ == '__main__':

    tool = Doubanspider()
    tool.start_work()

