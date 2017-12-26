# -*- coding:utf-8 -*-

import urllib2

URLERRORCODE = 777

def can_use_proxy(request, openner, URLERRORCODE):
    try:
        response = openner.open(request,timeout=3)
        return response.getcode()
    except urllib2.HTTPError, err:
        return err.code
    except urllib2.URLError, err:
        return URLERRORCODE

if __name__ == '__main__':

    # 1.大量proxy free
    proxy_list = [
        {"https": "117.69.142.196:808"},
        {"http": "101.68.73.54:53281"},
        {"http": "113.87.161.227:8118"},
        {"http": "114.245.149.215:8118"},
        {"http": "195.5.40.109:3128"}
    ]

    # 验证有几个能用
    can_use_list = []

    for proxy in proxy_list:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        request = urllib2.Request("http://www.baidu.com", headers=headers)

        # 创建 代理处理器
        proxy_handler = urllib2.ProxyHandler(proxy)
        openner = urllib2.build_opener(proxy_handler)

        # 验证
        code = can_use_proxy(request, openner, URLERRORCODE)

        print code