# -*- coding:utf-8 -*-

# 掌握使用python向集合t3中插入1000条文档，文档的属性包括_id、name
# _id的值为0、1、2、3...999
# name的值为'py0'、'py1'...
# 查询显示出_id为100的整倍数的文档，如100、200、300...，并将name输出

# from pymongo import *
# import pymongo
#
# try:
#     client = MongoClient("localhost",27017)
#     db = client.py3
#     col = db.t3
#     for index in range(1000):
#         col.insert({"_id":index, "name":'py%s' %index})
#
#     print "ok"
#
# except Exception, e:
#     print e

# 查询显示出_id为100的整倍数的文档，如100、200、300...，并将name输出

# -*- coding:utf-8 -*-

from pymongo import *

try:
    client=MongoClient('localhost',27017)
    db=client.py3
    col=db.t3
    cursor=col.find({'$where':'function(){return this._id%100==0;}'},{'_id':0,'name':1})
    cursor=col.find({"$where":"function(){return this._id%100==0;}"},{"_id":0,"name":1})
    for item in cursor:
        print item['name']
except Exception,e:
    print e



