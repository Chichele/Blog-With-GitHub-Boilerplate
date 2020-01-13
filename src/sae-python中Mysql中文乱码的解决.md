---
layout: post
title: sae python中Mysql中文乱码的解决
categories: 
  - 瞎折腾
tags: 
  - sae
  - python
date: 2014-06-16 16:54:12
---

一开始我用的是：

```python
db=MySQLdb.connect(db=sae.const.MYSQL_DB,user=sae.const.MYSQL_USER,passwd=sae.const.MYSQL_PASS,host=sae.const.MYSQL_HOST,port=int(sae.const.MYSQL_PORT))
```

数据库编码与python代码的编码都已设为utf8，在PHPMyAdmin中添加中文记录，在网页查询显示中却显示乱码，我在网上各种搜索都找不到解决方法。最后终于发现在连接数据库时添加charset参数为utf8就可以了。。

```python
db=MySQLdb.connect(db=sae.const.MYSQL_DB,user=sae.const.MYSQL_USER,passwd=sae.const.MYSQL_PASS,host=sae.const.MYSQL_HOST,port=int(sae.const.MYSQL_PORT),charset='utf8')
```
