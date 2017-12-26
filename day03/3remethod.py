# -*- coding:utf-8 -*-


import re


# 1. split方法
p = re.compile(r'[\s\,\;]+')
print p.split('a,b;; c   d')
# ['a', 'b', 'c', 'd']

# 2. sub  替换字符和 调换顺序
p = re.compile(r'(\w+) (\w+)')
s = 'hello 123, hello 456'
# 替换内容
print p.sub(r'hello world', s)
# 调换分组顺序
print p.sub(r'\2 \1', s)

# 3. 匹配中文
title = u'你好,hello,世界'
pattern = re.compile(ur'[\u4e00-\u9fa5]+')
result = pattern.findall(title)
print result

