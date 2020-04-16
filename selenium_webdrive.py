from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Firefox()
#browser.get('http://www.baidu.com/')

#browser = webdriver.Chrome()
#browser.get('http://www.baidu.com/')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=C:\\Users\\zhangchen\\AppData\\Local\\Google\\Chrome\\User') #设置成用户自己的数据目录
# 使用headless无界面浏览器模式
#chrome_options.add_argument('--headless') #增加无界面选项
#chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl = "https://www.taobao.com/"
browser.get(mainUrl)

#f = open("taobao.html","wb")
#f.write(browser.page_source.encode("utf-8"))

#print(f"browser text = {browser.page_source}")
browser.quit()