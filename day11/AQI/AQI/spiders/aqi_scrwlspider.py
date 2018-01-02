# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
from AQI.items import AqiItem
import urllib


class AqiCrawlSpider(CrawlSpider):
    name = "aqi_crawlspider"
    allowed_domains = ["aqistudy.cn"]

    # 第一批请求：返回的响应不做解析，只会经过所有的Rule提取链接并发送链接请求
    start_url = ["https://www.aqistudy.cn/historydata/"]

    rules = [
        # 提取每个城市的链接（383）
        Rule(LinkExtractor(allow=r"monthdata\.php\?city="), follow=True),
        # 提取每个月的链接（48）
        Rule(LinkExtractor(allow=r"daydata\.php\?city="), callback="parse_day", follow=False)
    ]

    def parse_day(self, response):
        '''
            从Response里获取每个城市每个月的每一天数据，并存储到item
        '''
        url = response.url
        urlencode_city = url[url.find("=") +1 : url.rfind("&")]
        # 将url编码的字符串，转为UTF-8字符串
        city = urllib.unquote(urlencode_city)

        tr_list = response.xpath("//div[@class='row']//tr")
        tr_list.pop(0)

        for tr in tr_list:
            item = AqiItem()
            item['city'] = city.decode("utf-8")
            item['date'] = tr.xpath("./td[1]/text()").extract_first()
            item['aqi'] = tr.xpath("./td[2]/text()").extract_first()
            item['level'] = tr.xpath("./td[3]/span/text()").extract_first()
            item['pm2_5'] = tr.xpath("./td[4]/text()").extract_first()
            item['pm10'] = tr.xpath("./td[5]/text()").extract_first()
            item['so2'] = tr.xpath("./td[6]/text()").extract_first()
            item['co'] = tr.xpath("./td[7]/text()").extract_first()
            item['no2'] = tr.xpath("./td[8]/text()").extract_first()
            item['o3'] = tr.xpath("./td[9]/text()").extract_first()

            yield item

