from urllib.parse import urlencode
import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"} 

# 变动的是这两个参数，从start开始往后显示limit个数据 
formdata = { 
     'start':'0', 
     'limit':'10' 
} 

data = urlencode(formdata).encode("utf-8")
request = urllib.request.Request(url, data = data, headers = headers) 
response = urllib.request.urlopen(request) 

f = open("new.json","wb")
f.write(response.read())

#print(response.read().decode("utf-8"))