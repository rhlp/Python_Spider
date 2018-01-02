# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

# 将item数据存储csv文件的文件处理类
from scrapy .exporters import CsvItemExporter
import json
import pymongo


class AqiPipeline(object):
    def process_item(self, item, spider):
        item['crawl_time'] = str(datetime.utcnow())
        item['source'] = spider.name
        return item

class AqiCsvPipeline(object):
    def open_spider(self, spider):
        self.file_name = open("aqi_item.csv", "w")

        # 创建文件读写对象，参数为需要进行读写操作的文件对象
        self.csv_exporter = CsvItemExporter(self.file_name)
        # 开始执行item数据读写操作
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.csv_exporter.finish_exporting()
        self.file_name.close()


class AqiJsonPipeline(object):
    def open_spider(self, spider):
        self.file_name = open("aqi_item.json", "w")

    def process_item(self, item, spider):
        self.file_name.write(json.dumps(dict(item)) + ",\n")
        return item

    def close_spider(self, spider):
        self.file_name.close()


class AqiMongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="192.168.240.158", port=27017)
        self.db = self.client["AQI"]
        self.collection = self.db["item"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item




