# -*- coding:utf-8 -*-

# 导入urllib2
import urllib2
import random


url = "http://jingsupo.com"


# IE 9.0 的 User-Agent，包含在 user_agent里
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
]

user_agent = random.choice(ua_list)

headers = {"User-Agent": user_agent}

request = urllib2.Request(url, headers=headers)

# 向服务器发送这个请求
response = urllib2.urlopen(request)
print request.get_header("User-agent")

# 类文件对象支持,文件对象的操作方法,如read()方法读取文件全部内容,返回字符串
html = response.read()

# print html