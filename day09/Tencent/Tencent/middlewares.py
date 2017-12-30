# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from settings import USER_AGENT_LIST

import random

# 注意：　中间件中不需要return
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = user_agent

# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         # 1. 免费代理
#         #proxy = "http://120.26.167.140:16816"
#         # 2. 验证代理
#         proxy = "http://mr_mao_hacker:sffqry9r@120.26.167.140:16816"
#         request.meta['proxy'] = proxy
