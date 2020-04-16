import urllib.request

url = "https://www.12306.cn/mormhweb/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

request = urllib.request.Request(url, headers = headers)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))