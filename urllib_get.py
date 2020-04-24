# -*- coding: utf-8 -*-

# 导入urllib2 库
from urllib.parse import urlencode
import urllib.request

url = "http://www.baidu.com/s"
word = {"wd":"python"}
#转换成url编码格式（字符串）
word = urlencode(word) 
# url首个分隔符就是 ?
newurl = url + "?" + word   

print(newurl)

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

request = urllib.request.Request(newurl, headers=headers)

response = urllib.request.urlopen(request)
html = response.read()

f = open("baidu.html","wb")
f.write(html)