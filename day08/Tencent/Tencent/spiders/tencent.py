# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    # 爬虫名
    name = 'tencent'
    # 允许爬取的域名范围
    allowed_domains = ['hr.tencent.com']

    # 固定的url地址部分
    base_url = "http://hr.tencent.com/position.php?&start="
    # url地址的偏移量，每次自增10
    offset = 0
    # 起始url地址列表
    start_urls = [base_url + str(offset)]

    # 默认由parse()方法解析start_urls列表的响应
    def parse(self, response):
        # 提取所有职位信息的节点列表
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            # 迭代每个节点，并将数据保存到item对象里，每个item对象表示一条职位信息
            item = TencentItem()

            item['position_name'] = node.xpath("./td[1]/a/text()").extract_first()
            item['position_link'] = node.xpath("./td[1]/a/@href").extract_first()
            item['position_type'] = node.xpath("./td[2]/text()").extract_first()
            item['people_number'] = node.xpath("./td[3]/text()").extract_first()
            item['work_location'] = node.xpath("./td[4]/text()").extract_first()
            item['publish_times'] = node.xpath("./td[5]/text()").extract_first()

            yield item


        # 2. 通过下一页攻台获取所有数据
        '''
        # 如果返回不是None,表示到了最后一页
        # 如果返回None，表示没有到最后一页
        if not response.xpath("//a[@id='next' and @class='noactive']/@href").extract_first():
            next_link = "http://hr.tencent.com/" + response.xpath("//a[@id='next']/@href").extract_first()
            yield scrapy.Request(url=next_link, callback=self.parse)
        '''

        # 1. 通过offset偏移量控制url地址(不能动态获取最后一页)
        '''
        # 当偏移量到达2716，表示到了最后一页，就不在发送请求
        if self.offset <= 2716:
            # offset值每次自增10
            self.offset += 10
            # 构建请求对象，并交给引擎，引擎判断是一个请求对象，就交由调度处理
            # url是需要发送请求的url地址
            # callback表示该请求返回响应由指定的回调函数解析
            yield scrapy.Request(url=self.base_url + str(self.offset), callback=self.parse)

        '''





