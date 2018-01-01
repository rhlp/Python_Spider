# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 房间的id
    room_id = scrapy.Field()
    # 图片的链接
    image_src = scrapy.Field()
    # 主播的艺名
    nick_name = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片的保存的磁盘路径
    image_path = scrapy.Field()

    crawl_time = scrapy.Field()
    source = scrapy.Field()
