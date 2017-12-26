# -*- coding:utf-8 -*-

import urllib2
import urllib

import json

# 自己做一个翻译工具

def translate_data(keyword):
    # 1.url
    url = "http://fanyi.baidu.com/v2transapi"

    # 2.拼接参数
    formdata = {
        "from": "en",
        "to": "zh",
        "query": keyword,
        "transtype": "enter",
        "simple_means_flag": "3",
    }

    # 3.url 转码
    formdata_str = urllib.urlencode(formdata)

    # headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 4.构建请求对象 POST
    request = urllib2.Request(url, headers=headers)

    # 5.发送请求对象
    response = urllib2.urlopen(request)

    # 解析出结果 --json字符串
    data = response.read()
    # json 字符串
    print type(json)

    # 解析出数据:将字符串转换成 python对象 dict list
    dict_data = json.loads(data)
    print type(dict_data)

    result = dict_data["trans_result"]["data"][0]["dst"]
    print result

if __name__ == '__main__':
    # 1.用户输入
    keyword = raw_input("请输入翻译内容:")

    # 翻译结果
    translate_data(keyword)











