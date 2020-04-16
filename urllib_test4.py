import urllib.request

url = "https://www.jdlingyu.mobi/tag/%E5%96%B5%E7%B3%96%E6%98%A0%E7%94%BB"

# User-Agent
header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"} 
request = urllib.request.Request(url, headers = header)

#也可以通过调用Request.add_header() 添加/修改一个特定的header
request.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
# request.get_header(header_name="Connection")

response = urllib.request.urlopen(request)

#可以查看响应状态码
print(response.code)     
html = response.read()

f = open("new.html","wb")
f.write(html)