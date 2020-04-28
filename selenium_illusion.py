from selenium import webdriver
#from lxml import etree
from pyquery import PyQuery as pq
import time

def parse_html_boxes(text):
    doc = pq(text)
    grids = doc("#posts .post.grid").items()
    for grid in grids:
        div_img_a = grid.children('.img a')
        con_url = div_img_a.attr('href')
        con_title = div_img_a.attr('title')
        div_img_a_img = div_img_a.children('img')
        img_url = div_img_a_img.attr('data-src')
        type_text = grid.children('a').text()
        price_text = grid.children('.grid-meta .price').text()
        print(con_url)
        print(con_title)
        print(img_url)
        print(type_text)
        print(price_text)
    

# 获取一个浏览器对象
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题 (禁用gpu加速)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
br = webdriver.Chrome(chrome_options=chrome_options)

br.implicitly_wait(30)  # 隐性等待，最长等30秒 等待网页加载完成
# 设置窗口最大化
#br.maximize_window()
# 打开一个页面
br.get('https://www.iszg.cc/category/illusion')#https://www.iszg.cc

parse_html_boxes(br.page_source.encode("utf-8"))
#保存到文件
#f = open("iszg.html","wb")
#f.write(br.page_source.encode("utf-8"))\
'''
for i in range(1,2): 
    links=br.find_elements_by_link_text("下一页")
    link=links[0] 
    url=link.get_attribute('href')
    print(url)
    br.get(url) 
'''

time.sleep(1)
# 关闭窗口
br.close()
# 退出浏览器
#time.sleep(1)
br.quit()