---
layout: post
title: Requests模块中持续性的 Cookie 会话
categories: 
    - Tech
tags: 
    - python
date: 2014-08-28 11:41:38
---

Requests模块有如下优点：

*   国际化域名和 URLs
*   Keep-Alive &amp; 连接池
*   持续性的 Cookie 会话
*   类浏览器式的 SSL 加密认证
*   基本/精简式的身份认证
*   优雅的键/&#20540; Cookies
*   自动解压
*   Unicode 编码的响应主体
*   多段文件上传
*   连接超时
*   支持 .netrc
*   适用于 Python 2.6—3.3
*   安全的线程使用

其中最吸引我的就是“**持续性的 Cookie 会话**”功能，它接管了Cookie管理方面的工作，使我们在实现模拟登录时的工作量大大减少。下面我介绍一下如何使用这个特性：
首先建立一个会话：
```python
session = requests.session()
```

在这之后，如果是get方式打开链接，例如百度，则是：
```python
page = session.get("http://www.baidu.com")
```
这里的page变量是一个`Response`对象，page.content即是这个get请求返回的HTML内容。这时session自动将百度返回的Cookie给记录下来。

post请求同样类似。url，postData，headers，proxy等都可以作为参数，非常方便！

Requests模块本身就是为了易用而生，它的文档也非常简洁。
