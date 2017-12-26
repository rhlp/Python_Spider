# -*- coding:utf-8 -*-

import pymongo
import json

class json_to_mongo():
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 27017

    # 读取文件
    def __open_file(self):
        self.file = open("5tencent.json", "r")
        self.client = pymongo.MongoClient(host=self.host,port=self.port)

        # 创建数据库
        self.db = self.client["tencent"]
        # 创建集合
        self.collection = self.db["job"]

    # 关闭文件
    def __close_file(self):
        self.file.close()

    # 写入数据
    def write_database(self):
        self.__open_file()

        # 读取内容 json格式转换成python对象
        data = json.load(self.file)

        try:
            self.collection.insert(data)
            print "写入成功"

        except Exception, err:
            print err

        finally:
            self.__close_file()

if __name__ == '__main__':
    tool = json_to_mongo()
    tool.write_database()









