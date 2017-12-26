# -*- coding:utf-8 -*-

import urllib2

import urllib

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class Tiebaspider(object):
    def __init__(self, tiebaname, start_page, end_page):
        self.base_url = "https://tieba.baidu.com/f?"
        self.name = tiebaname
        self.start = start_page
        self.end = end_page
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self, url):
        try:
            request = urllib2.Request(url, headers=self.headers)

            response = urllib2.urlopen(request)

            if response.getcode() == 200:
                return response.read()
        except Exception, err:
            print err

    # 写入文件
    def write_file(self, data, page):
        filename = u"Tieba/" + str(page) + "页.html"
        print("%s正在下载中..." % filename)
        with open(filename, "w") as f:
            f.write(data)

    # 调度的方法
    def start_work(self):

        for page in range(self.start, self.end+1):
            pn = (page - 1) * 50
            params = {
                "kw": self.name,
                "pn": pn
            }

            # url 转码
            params_str = urllib.urlencode(params)

            url = self.base_url + params_str

            # 发送请求 写入本地数据
            data = self.send_request(url)
            self.write_file(data, page)


if __name__ == '__main__':

    # 1.贴吧名字
    tiebaname = raw_input("请输入贴吧名称:")

    # 2.开始页
    start_page = int(raw_input("开始页:"))

    # 3.结束页
    end_page = int(raw_input("结束页:"))

    # 4.拼接网址
    tool = Tiebaspider(tiebaname, start_page, end_page)

    tool.start_work()

    # 5.写入本地