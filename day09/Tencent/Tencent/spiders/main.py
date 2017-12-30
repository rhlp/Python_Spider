# -*- coding:utf-8 -*-

from scrapy import cmdline

# 将命令写到一个ｐｙ文件中右击运行可以运行爬虫
# cmdline.execute(["scrapy", "crawl", "baidu"])
cmdline.execute("scrapy crawl baidu".split())

# 将命令写到一个ｐｙ文件中右击运行可以创建爬虫
# cmdline.execute("scrapy genspider hello hello.com".split())