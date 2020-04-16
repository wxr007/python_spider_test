# -*- coding: utf-8 -*-

# 导入urllib2 库
import urllib.request

# 使用urllib2.urlopen()向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen("https://www.jdlingyu.mobi/tag/%E5%96%B5%E7%B3%96%E6%98%A0%E7%94%BB")

# 类文件对象的read()方法可读取文件全部内容，返回字符串
html = response.read()

f = open("new.html","wb")
f.write(html)