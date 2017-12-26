# -*- coding:utf-8 -*-

import requests
def request_base_use():

    url = "http://www.baudu.com"
    # 1.get 请求
    requests.get(url)

    # 2.get 带参数: 自动转码
    params = {
        "kw": 2
    }
    requests.get(url, params=params)

    # post 请求
    requests.post()

    # 4.带参数 自动转码
    formdata = {
        "kw":2
    }
    requests.post(url, data=formdata)

    # 5.ssl --ca证书, 忽略证书认证
    requests.get(url, verify = True)

    # 6.proxy 代理
    proxy = ("username", "pwd")
    requests.get(url, proxies=proxy)

    # 7.cookie -- session
    # 7.1创建session 是为了保存cookie
    session = requests.session()

    # 7.2发送登录 --cookie
    session.post(url)

    # 7.3
    session.post(data_url)

if __name__ == '__main__':
    pass


