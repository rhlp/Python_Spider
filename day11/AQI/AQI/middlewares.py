# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver

import scrapy

class SeleniumMiddleWare(object):
    def process_request(self, request, spider):
        if "daydata" in request.url:
            driver = webdriver.Chrome()
            driver.get(request.url)

            html = driver.page_source
            driver.quit()
            # 直接返回一个Response对象给引擎，引擎会认为这个是下载器返回的响应，那么就默认给Spider进行解析处理
            # 那么表示该请求不再通过下载器下载，而是通过Chrome渲染后再返回
            return scrapy.http.HtmlResponse(url=request.url, body=html.encode("utf-8"), encoding="utf-8",
                                            request=request)
