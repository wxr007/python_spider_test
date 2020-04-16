# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import urllib.request

# POST请求的目标URL
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}

formdata = {
"i":" python",
"from":"AUTO",
"to":"AUTO",
"smartresult":" dict",
"client":" fanyideskweb",
"salt":" 15082966550971",
"sign":" 2a6d78290492d163dbd6803b29e2489c",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_ENTER",
"typoResult":"true"
}

data = urlencode(formdata).encode("utf-8")

request = urllib.request.Request(url, data = data, headers = headers)
response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))