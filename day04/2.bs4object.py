# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

def bs_object():
    html = """
     <html><head><title>The Dormouse's story</title></head>
     <body>
     <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
     <p class="story">Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
     and they lived at the bottom of a well.</p>
     <p class="story">...</p>
     """
    # 转换类型,转化文档类型为解析类型(不指定解释器会报warning的错误)
    soup = BeautifulSoup(html, "lxml")

    # 1.Tag -->标签 -- 默认值返回的是 符合条件的第一个
    head = soup.head
    p = soup.p
    a = soup.a
    print p
    print p.name
    print a
    print a.name
    print a.attrs   # 获取属性,返回字典类型
    print type(p)   # <class 'bs4.element.Tag'>

    # 2.Navigablestring
    title = soup.title
    print title.string  # The Dormouse's story
    print type(title.string)  # <class 'bs4.element.NavigableString'>

    # BeautifulSoup
    print type(soup)  #<class 'bs4.BeautifulSoup'>

    # 4.Comment  -->注释的内容
    a = soup.a
    print a
    print a.string
    print type(a.string)   # <class 'bs4.element.Comment'>

if __name__ == '__main__':
    bs_object()