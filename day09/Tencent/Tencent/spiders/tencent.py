# -*- coding: utf-8 -*-
import scrapy

# 创建可以提取响应里链接的 linkExtractor 对象
from scrapy.linkextractors import LinkExtractor

# Rule 用来发送从linkExtractor对象提取的链接
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']

    #### 1. start_url里的链接发送后，返回的响应会经过每一个Rule提取链接，但是没有回调函数进行页面解析
    start_urls = ['http://hr.tencent.com/position.php?&start=0']


    #### 2. 每一个follow=True的响应都会经过所有Rule进行链接提取。
    ####    如果符合allow规则 则提取链接，如果不符合则不提取链接，所以不用担心。
    ####    如果follow=False，则提取链接

    rules = (
        #　－提取列表页的url并构建请求发送，返回的响应需要回调函数解析，同时继续经过所有的Rule跟进提取链接
        Rule(LinkExtractor(allow=r'start='), callback='parse_item', follow=True),
        #  -提取详情页的url地址，并构建请求发送，返回的响应需要回调函数解析，但是不在跟进提取链接
        Rule(LinkExtractor(allow=r'position_detail\.php\?id='), callback='parse_item')

        # 如果callback有回调函数，默认follow=False
        # 如果callback没有回调函数,默认follow=True

        # 3. Ruel适合深度优先的爬虫，通过多层RUle跳板，找到最后包含数据的页面
        # Rule(LinkExtractor(allow=r'体育（第一级）')),
        # Rule(LinkExtractor(allow=r'NBA（第二级）')),
        # Rule(LinkExtractor(allow=r'球员信息（第三级）'), callback="parse_item"),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
