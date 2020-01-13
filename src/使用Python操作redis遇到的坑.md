---
layout: post
title: 使用Python操作redis遇到的坑
date: 2015-05-11 00:37:15
categories: 
  - python
tags: 
  - python
  - redis
---
## 写在前面
基于Python3.4，往redis里插入数据后再读出来时所有键与值都是byte类型的，就是说如果你要使用这些值全部都得转换编码！想想就崩溃！但又想想肯定会有简单的解决方法...

## 问题解决
于是我查看了python-redis连接redis的参数，发现了`decode_responses`，默认值为False，从参数名上来看好像就是它了。好了我不扯淡了其实最后证明就是它！我将它设置为True就ok了。
```
redis.StrictRedis(host=db_host, port=db_port, password=db_password, decode_responses=True)
```

最后有点不理解的是，这种有用的参数为什么默认值为False。。。