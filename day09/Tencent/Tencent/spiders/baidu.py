# -*- coding: utf-8 -*-
import scrapy
import logging
# 老式用法
# from carapy import log


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # print "--" *20
        # print "hello world"
        logging.info("hello world")
        logging.warning("This is a Warning")

        logging.log(logging.ERROR, "This is a Error")
