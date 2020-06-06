# -*- coding: utf-8 -*-
import requests
import jsonpath

f = open('cookie.txt')
cookie_json_str = f.read()

print(cookie_json_str)

headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Host": "mp.weixin.qq.com",
"Referer": "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=1224620909&lang=zh_CN"
#"Cookie": "防止cookie过期，爬虫前，设置自己刚获取的cookie值"
       }
'''
for i in range(2):
    url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin={}&count=5&fakeid=MzU2MDgxNTgxMA==&type=9&query=&token=1224620909&lang=zh_CN&f=json&ajax=1".format(str(i * 5))

    response = requests.get(url, headers = headers)
    print(response.text)

    jsonRes = response.json()

    titleList = jsonpath.jsonpath(jsonRes, "$..title")
    urlList = jsonpath.jsonpath(jsonRes, "$..link")

    # 遍历 构造可存储字符串
    for index in range(len(titleList)):
        title = titleList[index]
        url = urlList[index]

        scvStr = "%s,%s,\n" % (title, url)
        with open("info.csv", "a+", encoding="gbk", newline='') as f:
            f.write(scvStr)
'''