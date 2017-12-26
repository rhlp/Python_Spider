# -*- coding:utf-8 -*-
import requests
from lxml import etree



class TiebaSpider(object):
    def __init__(self, name, sp, ep):
        self.url = 'https://tieba.baidu.com'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.name = name
        self.sp = sp
        self.ep = ep
        self.first_xpath = '//ul[@id="thread_list"]/li[@class="j_thread_list clearfix"]/div/div/div/div/a/@href'
        self.secend_xpath = '//div[@class="pb_content clearfix"]//div[@class="l_post l_post_bright j_l_post clearfix"]//img[@class="BDE_Image"]/@src'

    def get_data(self, url, params={}):

        response = requests.get(url, params=params, headers=self.headers)

        return response.content

    def filter(self, data, content):
        html_data = etree.HTML(data)

        data_list = html_data.xpath(content)

        return data_list

    def save_file(self, filename, data):
        print '1'
        with open('tieba/'+filename, 'w') as f:
            f.write(data)

    def start_app(self):
        for i in range(self.sp, self.ep+1):
            params = {
                'kw': self.name,
                'pn': (i-1) * 50
            }
            data = self.get_data(self.url+'/f?', params)

            data_list = self.filter(data, self.first_xpath)

            for url in data_list:
                print url
                data = self.get_data(self.url+url)
                data_list = self.filter(data, self.secend_xpath)
                for url in data_list:
                    data = self.get_data(url)
                    self.save_file(url[-15:], data)


if __name__ == '__main__':
    name = raw_input('请输入贴吧名:')
    sp = raw_input('请输入开始页面')
    ep = raw_input('请输入结束页面')
    spider = TiebaSpider(name, int(sp), int(ep))

    spider.start_app()