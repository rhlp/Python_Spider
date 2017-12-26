# -*- coding:utf-8 -*-

import urllib2

def web_auth_openner():
    # 1.url
    url = "http://60.205.187.28/1.php"

    # 密码管理器
    pwd_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # 添加用户名和密码
    # realm, None
    # uri, url
    # user,
    # passwd
    pwd_manager.add_password(None, uri=url, user="admin", passwd="admin")


    # 1.自定义 具有 web认证的处理器
    web_handler = urllib2.HTTPBasicAuthHandler(pwd_manager)

    # 2.根据处理自定义openner
    web_openner = urllib2.build_opener(web_handler)


    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 3.request
    request = urllib2.Request(url, headers=headers)

    # 自定义的openner.open
    # urllib2.urlopen(request)
    response = web_openner.open(request)

    # 返回数据
    print response.read()


if __name__ == '__main__':
    web_auth_openner()


