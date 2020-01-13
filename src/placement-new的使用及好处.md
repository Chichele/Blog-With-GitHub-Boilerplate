---
layout: post
title: placement new的使用及好处
categories: 
  - Tech
tags: 
  - C++
date: 2014-08-17 16:59:02
---

详细的介绍可以看这几篇文章：

[C++中placement new操作符（经典）](http://blog.csdn.net/zhangxinrun/article/details/5940019)

[Placement new的用法及用途](http://www.cppblog.com/kongque/archive/2010/02/20/108093.html)

[（转）遵循placement new的用法规范](http://www.cnblogs.com/felixYeou/archive/2009/04/15/1436209.html)

归纳一下placement new的好处：

1. **在已分配好的内存上进行对象的构建，构建速度快。**

1. **可以反复利用同一块已分配好的内存，有效的避免内存碎片问题。**

1. **建立对象数组时，能够调用带参数的构造函数。**
