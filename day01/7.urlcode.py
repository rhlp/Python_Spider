# -*- coding:utf-8 -*-

import urllib2

import urllib

def load_data_with_search(keyword):

    # 1.url
    # url = "https://www.baidu.com/s?wd=" + keyword
    # url = "https://www.baidu.com/s?wd=%s" % keyword


    # 转码--> 将字典 转换成带= 的字符串
    url = "https://www.baidu.com/s?"
    params = {
        "wd": keyword
    }

    # 需要注意:字符串 和 字典 不能直接拼接
    # real_url = url + str(params)

    # 需要使用 urllib 库转码
    params_str = urllib.urlencode(params)
    real_url = url + params_str
    print real_url

    # 2.user-agent
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.请求对象
    request = urllib2.Request(url, headers=headers)

    # 4.发送请求
    response = urllib2.urlopen(request)

    # 返回数据
    return response.read()

if __name__ == '__main__':
    # 请求用户输入 想搜索的内容
    keyword = raw_input("请输入搜索的内容:")
    data = load_data_with_search(keyword)

    with open("7.urlcode.html", "w") as f:
        f.write(data)



