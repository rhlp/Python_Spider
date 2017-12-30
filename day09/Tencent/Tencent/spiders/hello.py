# -*- coding: utf-8 -*-
import scrapy


class HelloSpider(scrapy.Spider):
    name = 'hello'
    allowed_domains = ['hello.com']
    start_urls = ['http://hello.com/']

    def parse(self, response):
        pass
