# -*- coding:utf-8 -*-

# AQI 所需要 数据字段分析
'''
https://www.aqistudy.cn/historydata/


# 取所有城市的链接
//div[@class='all']//li/a/@href

https://www.aqistudy.cn/historydata/

# 取每个城市的每个月的链接
//ul[@class='unstyled1']//li


# 取每个月的每天数据

tr_list = //div[@class='row']//tr

tr_list.pop(0)

for tr in tr_list:
    tr.xpath("./td[1]/text()")
    tr.xpath("./td[2]/text()")
    tr.xpath("./td[3]/span/text()")
    tr.xpath("./td[4]/text()")
    tr.xpath("./td[5]/text()")
    tr.xpath("./td[6]/text()")
    tr.xpath("./td[7]/text()")
    tr.xpath("./td[8]/text()")
    tr.xpath("./td[9]/text()")


date
aqi
level
pm2_5
pm10
so2
co
no2
o3
'''