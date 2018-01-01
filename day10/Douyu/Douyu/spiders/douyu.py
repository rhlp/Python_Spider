# -*- coding: utf-8 -*-
import scrapy
import json

from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']

    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']

        if data_list:
            for data in data_list:
                item = DouyuItem()
                item['room_id'] = data['room_id']
                item['image_src'] = data['vertical_src']
                item['nick_name'] = data['nickname']
                item['city'] = data['anchor_city']

                # yield scrapy.Request(url=item['image_src'], meta = {"image_name" : item['nick_name']}, callback = self.parse_image)

                yield item
            # 处理下一页的情况
            self.offset += 20
            yield scrapy.Request(url=self.base_url + str(self.offset), callback=self.parse)

    '''
    def parse_image(self, response):
        with open(response.meta['image_name'] + ".jpg", "wb") as f:
            f.write(response.body)
    '''




