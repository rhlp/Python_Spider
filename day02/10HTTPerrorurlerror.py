# -*- coding:utf-8 -*-

import urllib2

if __name__ == '__main__':

    try:
        resopnse = urllib2.urlopen("http://www.itcast.com")

    except urllib2.HTTPError, err:
        print err.code
    # 双重判断错误
    except urllib2.URLError, err:
        print err


