from selenium import webdriver
import time

# 获取一个浏览器对象
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题 (禁用gpu加速)

br = webdriver.Chrome(chrome_options=chrome_options)

br.implicitly_wait(30)  # 隐性等待，最长等30秒 等待网页加载完成
# 打开一个页面
br.get('https://www.iszg.cc/')

f = open("iszg.html","wb")
f.write(br.page_source.encode("utf-8"))

time.sleep(1)
# 关闭窗口
br.close()
# 退出浏览器
time.sleep(1)
br.quit()