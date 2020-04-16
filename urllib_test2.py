# -*- coding: utf-8 -*-

# 导入urllib2 库
import urllib.request

# url 作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request("https://www.jdlingyu.mobi/tag/%E5%96%B5%E7%B3%96%E6%98%A0%E7%94%BB")

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
response = urllib.request.urlopen(request)

html = response.read()

f = open("new.html","wb")
f.write(html)