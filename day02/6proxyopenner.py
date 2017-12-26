# -*- coding:utf-8 -*-

import urllib2

# 创建具有 代理IP功能 的处理器

def proxy_openner():
    # proxy = {"协议":"IP:port"}
    # 免费的代理：不稳定 不知道什么时候行
    proxy = {"http": "121.232.145.246:9000"}

    # 建议使用付费的代理
    proxy = {"协议":"用户名:密码@IP:port"}

    proxy = {"http": "mr_mao_hacker:sffqry9r@120.27.218.32:16816"}

    # 1.创建具有 proxy功能的处理器
    proxy_handler = urllib2.ProxyHandler(proxy)

    # 2.根据处理器创建openner
    openner = urllib2.build_opener(proxy_handler)


    # 1.url
    url = "http://www.baidu.com"

    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.request
    request = urllib2.Request(url, headers=headers)

    # 4.使用自己定义的openner.open()发送请求
    response = openner.open(request)

    # 5.返回数据
    print response.read()

if __name__ == '__main__':
    proxy_openner()
