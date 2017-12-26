# -*- coding:utf-8 -*-

import urllib2

#创建处理器  自定义openner
def custom_openner():

    # 1.创建处理器
    # # 构建一个HTTPHandler 处理器对象，支持处理HTTP请求，同时开启Debug Log，debuglevel 值默认 0
    handler = urllib2.HTTPHandler(debuglevel=1)

    # 2.根据处理器自定义openner
    openner = urllib2.build_opener(handler)

    # 使用我们自己定义的openner.open()发送请求
    # url
    url = "http://www.baidu.com"

    # headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # request
    request = urllib2.Request(url, headers=headers)

    # 发送response
    response = openner.open(request)

    print response.read()

if __name__ == '__main__':

    custom_openner()
