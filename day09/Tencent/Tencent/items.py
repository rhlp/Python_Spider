# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    """
        保存列表页的item
    """
    # 职位名
    position_name = scrapy.Field()
    # 职位详情链接
    position_link = scrapy.Field()
    # 职位类别
    position_type = scrapy.Field()
    # 招聘人数
    people_number = scrapy.Field()
    # 工作地点
    work_location = scrapy.Field()
    # 发布时间
    publish_times = scrapy.Field()

    # 数据源
    source = scrapy.Field()
    # 抓取数据的时间
    crawl_time = scrapy.Field()

class PositionItem(scrapy.Item):
    """
        保存详情页的item
    """
    # 工作职责
    position_zhize = scrapy.Field()
    # 工作要求
    position_yaoqiu = scrapy.Field()
    # 数据源
    source = scrapy.Field()
    # 抓取数据的时间
    crawl_time = scrapy.Field()

