# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from mySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    # 爬虫的识别名称
    name = 'itcast'
    # 允许爬虫爬取的域名范围
    allowed_domains = ['itcast.cn']
    # 爬虫启动时，发送的第一批url地址列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']



    # 如果需要保存数据到json/csv/xml文件格式，可以先将所有item数据放到列表里，在return这个列表
    # 执行爬虫的时候，可以通过 -o 输出到指定的文件里，csrapy会识别文件的后缀，并存储为指定的格式
    # parse（）默认解析start_urls里发送的请求对应的响应
    def parse(self, response):
        # with open("teacher.html", "w") as f:
        #     f.write(response.text)
        node_list = response.xpath("//div[@class='li_txt']")
        print node_list
        item_list = []
        for node in node_list:
            item = MyspiderItem()
            item['name'] = node.xpath("./h3/text()").extract_first()
            item['level'] = node.xpath("./h4/text()").extract_first()
            item['info'] = node.xpath("./p/text()").extract_first()
            item_list.append(item)

        return item_list



