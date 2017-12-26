# -*- coding:utf-8 -*-

import urllib2
import ssl

# urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:590)>

#如果 网站没有CA证书 访问受限制  可以 告诉系统忽略
def ssl_load_data():

    # url
    url = "https://www.12306.cn/mormhweb/"

    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.request
    request = urllib2.Request(url, headers=headers)

    # 4.发送请求
    # 主动告诉系统 忽略证书ssl
    context = ssl._create_unverified_context()
    response = urllib2.urlopen(request, context=context)

    with open("4ssl.html", "w") as f:
        f.write(response.read())

if __name__ == '__main__':
    ssl_load_data()





