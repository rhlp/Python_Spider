# -*- coding:utf-8 -*-

import urllib2
import urllib
import cookielib

def send_request():

    # 具有cookie 的openner

    # cookjar 用来保存这个cookie
    cookjar = cookielib.CookieJar()

    # 1.创建处理器
    cook_handler = urllib2.HTTPCookieProcessor(cookjar)

    # openner
    cook_openner = urllib2.build_opener(cook_handler)

    # headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 1.登录成功 有cookie
    login_url = "http://renren.com/PLogin.do"

    # 2.参数
    formdata = {
        "email": "mr_mao_hacker@163.com",
        "password": "alarmchime"
    }
    # 转码
    formdata_str = urllib.urlencode(formdata)
    request = urllib2.Request(login_url, data=formdata_str, headers=headers)

    # 3.先发送登录请求 获取保存的cookie
    cook_openner.open(request)


    # 拿着有登录成功的 cookie的openner 发送数据请求
    # 1.url -- 直接访问的 登录之后的数据
    data_url = "http://www.renren.com/410043129/profile"
    data_request = urllib2.Request(data_url, headers=headers)


    response = cook_openner.open(data_request)

    # 返回数据
    return response.read()

def write_file(data):
    with open("9renren.html", "w") as f:
        f.write(data)


if __name__ == '__main__':
    data = send_request()
    write_file(data)