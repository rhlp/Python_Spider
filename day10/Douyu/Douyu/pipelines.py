# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class DouyuImagesPipeline(ImagesPipeline):
    # 发送每个图片的请求，并自动保存到settings里IMAGE_STORE指定的路径下
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_src'])





'''
class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item
'''