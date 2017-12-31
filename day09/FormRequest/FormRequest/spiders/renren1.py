# -*- coding: utf-8 -*-
import scrapy


class Renren1Spider(scrapy.Spider):
    name = 'renren1'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/PLogin.do']

    # 如果重写了start_requests，那么start_urls列表可有可无
    # 如果没有重写，必须提供start_urls列表
    # 1.发送登陆页面的post请求
    # 登陆成功后scrapy会记录登陆状态的cookie,那么之后发送的请求就会附带cookie
    def start_requests(self):
        login_url = 'http://www.renren.com/PLogin.do'
        # FormRequest()表示构建一个post请求
        yield scrapy.FormRequest(
            # url为发送post请求的url地址
            url = login_url,
            # formdata表示发送post请求是提交的表单数据
            formdata={"email": "mr_mao_hacker@163.com", "password": "alarmchime"},
            callback=self.parse
        )

    # 2.带着cookie发送其他页面的get请求，并制定回调函数处理
    def parse(self, response):
        url_list = [
            "http://www.renren.com/410043129/profile",
            "http://www.renren.com/429732223/profile"
        ]
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        file_name = response.xpath("//title/text()").extract_first() + ".html"
        with open(file_name, "w") as f:
            f.write(response.body)
