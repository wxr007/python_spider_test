import urllib.request

url = "https://www.jdlingyu.mobi/tag/%E5%96%B5%E7%B3%96%E6%98%A0%E7%94%BB"

#  User-Agent，可以从网上找，也可以自己使用浏览器抓包获取
header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"} 

# 起构造Request请求，
request = urllib.request.Request(url, headers = header)

# 向服务器发送这个请求
response = urllib.request.urlopen(request)

html = response.read()
f = open("new.html","wb")
f.write(html)