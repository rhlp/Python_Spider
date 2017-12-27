# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 姓名
    name = scrapy.Field()
    # 职称
    level = scrapy.Field()
    # 信息
    info = scrapy.Field()
