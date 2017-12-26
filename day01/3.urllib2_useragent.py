# -*- coding:utf-8 -*-

# 导入urllib2
import urllib2

url = "http://www.itcast.cn"


# IE 9.0 的 User-Agent，包含在 user_agent里
user_agent = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

# url连同headers,一起构造Request请求,这个请求将附带 IE9.0 浏览器的User-agent
request = urllib2.Request(url, headers=user_agent)

# 向服务器发送这个请求
response = urllib2.urlopen(request)

# 类文件对象支持,文件对象的操作方法,如read()方法读取文件全部内容,返回字符串
html = response.read()

print html