---
layout: post
title: Web自动化测试工具——Selenium
categories: 
    - Tech
tags: 
    - 测试
    - python
date: 2014-09-18 23:49:59
---

在最近的Web课程设计上我接触到了`Selenium`这款Web自动化测试工具，它可以通过一系列`find_element()`方法定位到目标元素，对其发送模拟按键操作，使操作自动化。

首先，使用pip安装Selenium的Python模块。

`find_element_by_name()`方法就是通过`name`属性来定位元素，然后通过`send_keys()`发送模拟按键。基于这样的操作基本可以完成各种web下的模拟操作。下面是我写的例程:

```python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/usr/local/lib/python2.7/dist-packages/selenium/webdriver/chrome/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://localhost:8000/")
driver.get("http://localhost:8000/login")
assert "Bookstore" in driver.title
elem_username = driver.find_element_by_name("username")
elem_username.send_keys("tiger1")
elem_password = driver.find_element_by_name("password")
elem_password.send_keys("tiger1")
elem_password.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
```

如果遇到以下错误

`selenium.common.exceptions.WebDriverException: Message: 'ChromeDriver executable needs to be available in the path.`

解决方法在[http://selenium-python.readthedocs.org/faq.html#how-to-use-chromedriver](http://selenium-python.readthedocs.org/faq.html#how-to-use-chromedriver)
