---
layout: post
title: Python爬取京东商品数据
categories: 
	- 瞎折腾
tags: 
	- python
date: 2014-06-16 17:08:41
---

对京东某一商品信息页面的HTML代码进行分析，可以发现它的图书产品信息页面都含有这样一段代码（不同类的商品页面有些不同）：

```javascript
window.pageConfig={compatible:true,searchType: 1,product:{"skuid":"11408255","name":"\u4f17\u795e\u7684\u536b\u661f\uff1a\u4e2d\u56fd\u7981\u533a","skuidkey":"0337880E5D0F419E033111D988169617","href":"http:\/\/item.jd.com\/11408255.html","src":"g14\/M01\/13\/0F\/rBEhVVMPSugIAAAAAAViPV7x4XAAAJS4gLble8ABWJV204.jpg","jqimg":"http:\/\/img11.360buyimg.com\/n0\/g14\/M01\/13\/0F\/rBEhVVMPSugIAAAAAAViPV7x4XAAAJS4gLble8ABWJV204.jpg","wMaprice":"32.00","wMeprice":"23.40","cat":[1713,9340,9346],"brand":"","tips":false,"type":1,"n":false,"g":false}};
```

显然这就是我们需要的商品信息，Python代码如下：

```python
import json
import re
import urllib
for i in range(11348876,11348999):#数字代表京东商品编号
	URL='http://item.jd.com/%s.html'%(i)
	page=urllib.urlopen(URL).read()
	idx=page.find('product:')
	if(idx>=0):
		idx+=8
		res=re.search(r'{.+?}',page[idx:])    #用正则表达式匹配
		text=json.loads(res.group())    #用json读取
		print("%s,%s,%s,%s,%s"%(text['skuid'],text['wMaprice'],text['name'],text['href'],text['jqimg']))
```