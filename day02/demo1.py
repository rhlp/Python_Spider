# -*- coding:utf-8 -*-

import urllib2

import urllib

# 获取ajax加载的内容
# ajax请求一般返回给网页的JSON文件,只要对AJAX请求,就能返回JSON数据

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&"

headers = {"User-Agent": "Mozilla...."}


# 变动的是这两个参数,从start开始往后面显示limit
formdata = {
    "start": "0",
    "limit": "10"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url + data, headers=headers)

response = urllib2.urlopen(request)

print response.read()

