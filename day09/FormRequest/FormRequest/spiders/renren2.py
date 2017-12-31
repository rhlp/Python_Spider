# -*- coding: utf-8 -*-
import scrapy


class Renren2Spider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    start_urls = [
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/429732223/profile"]

    cookies = {
        "anonymid":"jbbjvcqslf53au",
        "_r01_":"1",
        "__utma":"151146938.1010603587.1513562321.1513562321.1513562321.1",
        "__utmz":"151146938.1513562321.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ln_uact=mr_mao_hacker@163.com",
        "_ga":"GA1.2.1010603587.1513562321",
        "depovince":"GW",
        "JSESSIONID":"abcCXDu2iULkpakKVqQcw",
        "ick_login":"a7f7825c-fd75-41cb-96da-8439f8d95e8a",
        "jebe_key":"f7d40357-7f9f-4d11-9cc5-f25dca61c884%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1513563205145%7C1%7C1514685003137",
        "first_login_flag":"1",
        "ln_hurl":"http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg",
        "loginfrom":"syshome",
        "ch_id":"10016",
        "wp":"1",
        "jebecookies":"9712b63b-5acc-405d-8a12-0241ce115e26|||||; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "p":"94180e440421e5db02d5f820609120119",
        "t":"9a7f5b520ca0d75605c07a91034ee6599",
        "societyguester":"9a7f5b520ca0d75605c07a91034ee6599",
        "id":"327550029",
        "xnsid":"55b8e257",
        "wp_fold":"0"

    }

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(
                url = url,
                cookies=self.cookies,
                callback=self.parse,
                # 不做去重
                dont_filter=True
            )

    def parse(self, response):
        file_name = response.xpath("//title/text()").extract_first() + ".html"
        with open(file_name, "w") as f:
            f.write(response.body)

