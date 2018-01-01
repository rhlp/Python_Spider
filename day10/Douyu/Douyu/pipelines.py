# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE
import os
import logging
import pymongo
from datetime import datetime


class DouyuImagesPipeline(ImagesPipeline):
    # 发送每个图片的请求，并自动保存到settings里IMAGE_STORE指定的路径下
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_src'])

    def item_completed(self, results, item, info):
        # print "**" * 30
        # print results
        # return item
        '''打印结果
        [(True, {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2017/12/02/476004_20171202043700_big.jpg',
        'path': 'full/7693f8e9005f0793eb074818ef3bbcc4f34aab0c.jpg',
        'checksum': '271177c954f305637002d75e65faeac9'})]
        '''

        # 返回图片原来名字的字符串
        image_path = [x['path'] for ok, x in results if ok][0]

        # 设定好保存图片的路径和文件名
        new_name = IMAGES_STORE + item['nick_name'] + ".jpg"
        item['image_path'] = new_name

        # 将原图片名修改为新的图片的名
        try:
            os.rename(IMAGES_STORE + image_path, item['image_path'])
        except:
            logging.error("图片已被修改..")

        return item

class DouyuMongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        self.db = self.client['Douyu']
        self.collection  = self.db['item']

    def process_item(self, item, spider):
        item['source'] = spider.name
        item['crawl_time'] = str(datetime.utcnow())
        self.collection.insert(dict(item))
        return item

'''
class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item
'''