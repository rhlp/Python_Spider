# -*- coding:utf-8 -*-

import urllib2

class Doubanspider(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action="
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self):
        try:
            request = urllib2.Request(self.base_url, headers=self.headers)
            response = urllib2.urlopen(request)
            if response.getcode() == 200:
                return response.read()
        except Exception, err:
            print err

    # 保存本地文件
    def write_file(self, data):
        with open("1doubanhome.html", "w") as f:
            f.write(data)

    # 调度的方法
    def start_work(self):
        data = self.send_request()
        self.write_file(data)

if __name__ == '__main__':
    tool = Doubanspider()
    tool.start_work()







