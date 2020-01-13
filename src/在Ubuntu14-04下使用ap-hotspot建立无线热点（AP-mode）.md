---
layout: post
title: 在Ubuntu14.04下使用ap-hotspot建立无线热点（AP mode）
categories: 
    - 瞎折腾
tags: 
    - ubuntu
date: 2014-08-15 22:36:02
---

从`https://launchpad.net/~nilarimogard/+archive/ubuntu/webupd8/+packages` 下载最新版ap-hotspot并安装，我使用的是`ap-hotspot - 0.3.1-1~webupd8~0`。终端下执行`sudo ap-hotspot configure`

这一步会检查ubuntu的网络和WIFI接口，确定后会提示你配置热点，输入ssid和密码之类的就行了

接着执行`sudo ap-hotspot start`即可。


----------


可是现实总是残酷的，在Ubuntu14.04下这样还不能够成功。因为自带的新版hostapd有bug，所以我们需要降级到一个可用的旧版本。参考链接：[http://askubuntu.com/questions/464178/ap-hotspot-not-creating-in-kubuntu-14-04](http://askubuntu.com/questions/464178/ap-hotspot-not-creating-in-kubuntu-14-04)

按这链接操作，安装好旧版hostapd之后，使用ap-hotspot会提示没有安装，需要重新安装并配置。最终即可成功建立AP热点。