---
layout: post
title: 贴吧大召唤术——Python实现提取贴吧页面的用户id
categories: 
  - 瞎折腾
tags: 
  - python
date: 2014-05-03 15:31:42
---

前几天就想写一个python脚本实现从百度贴吧任意帖子页面获取该页面上的用户id。
一开始我打算用正则表达式查找`<a data-field>`标签，但多次尝试后被搞晕了！！html代码里面的转义实在太麻烦了！（好吧，其实只是我没经验））

后来尝试用`BeautifulSoup`解析html，顺利得到用户id了，但是从得到的结果发现，有些用户id居然没有得出来，分析半天才发现原来是百度贴吧把html的一半给以`<!-->`标签注释掉了，估计是为了优化页面的加载。但正是这个原因使得我无法直接使用`BeautifulSoup`解析html获取目标结果了。

于是我又想找找有没有别的第三方模块可以处理html注释部分，尝试了`lxml.html`模块，同样无果。

最终只有回到最初的方法——正则表达式，搞定！


```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'tigerstudent'
import urllib
import re
import json

# 因为该网页是 gbk编码的，所以首先从gbk编码转为python内部的unicode编码
page=urllib.urlopen(r'http://tieba.baidu.com/p/3014774907').read().decode('gbk')
# 这里涉及到正则表达式的贪婪匹配，所以用(.+?)而不用(.+)
res=re.findall(r"data-field=\'(.+?)\'",page)
for i in res:
    i=i.replace(u'"',u'"')
    #i=i.replace(u'false',u"False")这行代码没必要，因为python的False在json格式中表示为false
    final=json.loads(i)
    if(final and final.get('un')):#若final不为None且含有'un'元素则输出
        print final.get('un')
print res[0]    # 从这里输出的结果可以知道，在上面对i的修改并没有真正修改res的内容
print type(res[0])
```

虽然最终没有用`BeautifulSoup`和`lxml.html`模块解决...
