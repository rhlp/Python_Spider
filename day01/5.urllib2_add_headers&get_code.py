# -*- coding:utf-8 -*-

import urllib2

def load_data():
    # 1.url
    url = "http://www.baidu.com"

    # 2.构建请求对象
    request =urllib2.Request(url)

    # 动态添加 报头 user-agent
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    request.add_header("Connection", "keep-live")

    # 3.发送请求
    response = urllib2.urlopen(request)

    # 获取报头的内容
    # 注意点:key  除了首字母是大写 其他的必须是小写
    print request.get_header("User-agent")
    print request.get_header("Connection")

    # 读取
    data = response.read()

    # 获取响应代码
    response_code = response.getcode()
    print response_code

    # 获取请求地址
    real_url = response.geturl()
    print real_url

    # 写入文件
    if response_code == 200:
        with open("5.urllib2_add_headers&get_code.html", "w") as f:
            f.write(data)

if __name__ == '__main__':
    load_data()
