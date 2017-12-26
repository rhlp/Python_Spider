# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree

def parse_xsrf():
    # url
    url = "https://www.zhihu.com"

    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.发送请求
    response = requests.get(url, headers=headers, verify=False).content

    # 4.解析数据
    # # 4.1 bs4
    # soup = BeautifulSoup(response, "lxml")
    # # 列表
    # result = soup.select('input[name="_xsrf"]')
    # # 属性 value
    # xsrf = result[0].get("value")
    # print xsrf

    # 4.2 xpath
    html_data = etree.HTML(response)
    result = html_data.xpath('//input[@name="_xsrf"]/@value')
    # 属性value
    xsrf = result[0]
    print xsrf

if __name__ == '__main__':
    parse_xsrf()
