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

            return scrapy.http.HtmlResponse(url=request.url, body=html.encode("utf-8"),encoding="utf-8", request=request)

