# -*- coding:utf-8 -*-
import urllib2
import urllib


url = "https://movie.douban.com/j/chart/top_list?"
headers={"User-Agent": "Mozilla...."}

# 处理所有参数
formdata = {
    'type':'11',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'10'
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url + data, headers=headers)

response = urllib2.urlopen(request)

print response.read()