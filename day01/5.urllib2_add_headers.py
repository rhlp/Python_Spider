# -*- coding:utf-8 -*-

import urllib2

url = "http://www.itcast.cn"

# IE 9.0 的 User-Agent 为了伪装 修改 user-agent
# user_agent = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

# 2.构建对象
# request = urllib2.Request(url, headers=user_agent)

# 也可以通过调用Request.add_header() 添加/修改一个特定的header
request = urllib2.Request(url)
request.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
request.add_header("Connection", "keep-alive")

# 3.发送请求
response = urllib2.urlopen(request)

# 也可以通过调用Request.get_header()来查看header信息
user = request.get_header(header_name="Connetion")
print user

user = request.get_header("User-agent")
print user

# 返回数据
code = response.getcode()
print code
print response.code

html = response.read()

# print html


