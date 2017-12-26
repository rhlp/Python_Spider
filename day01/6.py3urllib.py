# -*- coding:utf-8 -*-

import urllib.request

def load_data_with_python3():
    # url
    url = "http://www.baidu.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 构建请求对象
    request = urllib.request.Request(url, headers=headers)

    # 发送请求
    response = urllib.request.urlopen(request)

    # 读取数据
    return response.read()

if __name__ == '__main__':
    data = load_data_with_python3()
    print(data)

