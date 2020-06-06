# -*- coding: utf-8 -*-

# 导入urllib2 库
from urllib.parse import urlencode
import urllib.request
import os

os.makedirs("download")

url = "https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00455-428.jpg"

urllib.request.urlretrieve(url,filename="download/meishi.jpg")