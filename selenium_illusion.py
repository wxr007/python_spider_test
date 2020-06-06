import os
import time
import pymysql
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import datetime

img_path = "E:/WorkSpace/Node/my_illusion_web/static/img"
html_path = "E:/WorkSpace/Node/my_illusion_web/static/html"

#创建图片目录
if os.path.exists(img_path) == False:
    os.makedirs(img_path)
#创建html目录
if os.path.exists(html_path) == False:
    os.makedirs(html_path)
#链接数据库
db = pymysql.connect("localhost","root","123456","illusion")
cursor = db.cursor()
#创建csv文件
csv = open("boxes.csv","w",encoding='utf-8')
#设置urllib.request的header
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;')]
urllib.request.install_opener(opener)
# 获取一个浏览器对象
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题 (禁用gpu加速)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
br = webdriver.Chrome(chrome_options=chrome_options)
#登录
def web_login():
    br.find_elements_by_class_name("signin-loader")[0].click()
    br.find_elements_by_id("user_login").clear()
    br.find_element_by_id('user_login').send_keys('wxr_007')
    br.find_elements_by_id("user_pass").clear()
    br.find_element_by_id('user_pass').send_keys('110llo120lzo')
    br.find_elements_by_name("submit")[0].click()
    time.sleep(1)

#保持box中的信息
def save_box_data(oid,con_title,img_url,type_text,price_text):
    filename = "{}/{}.jpg".format(img_path,oid)
    if os.path.exists(filename) == False:
        try:
            urllib.request.urlretrieve(img_url,filename) #下载缩略图
        except Exception as e:
            print(e)
    sql = "SELECT count(1) FROM content_table WHERE oid = '%s'" % (oid)
    print(sql)
    try:
        cursor.execute(sql)  # 执行sql语句
        db.commit()          # 执行sql语句
        results = cursor.fetchall()# 获取所有记录列表
        result = results[0][0]
    except Exception as e:
        print(e)
    #如果有数据则不用插入
    if result == 1:
        return
    resource_type = 1
    if type_text == '游戏下载':
        resource_type = 1
    elif type_text == '美女福利':
        resource_type = 2
    #插入数据库
    sql = "INSERT INTO content_table(oid, title, type, type_txt, price_txt) \
    VALUES ('%s', '%s', '%d', '%s',  '%s' )" % \
    (oid, con_title, resource_type, type_text, price_text)
    print(sql)
    try:
        cursor.execute(sql)  # 执行sql语句
        db.commit()          # 执行sql语句
    except Exception as e:
        print(e)
        db.rollback()        # 发生错误时回滚
    #写csv文件
    csv.write(oid+',\"'+con_title+'\",'+type_text+','+price_text+'\n')

#保存内容页面中的图片
def save_img_in_content(oid,org_img_url):
    #save_path = "{}/{}".format(html_path,oid) 
    save_path = os.path.join(html_path,"content_img",oid)
    if os.path.exists(save_path) == False:
        os.makedirs(save_path)
    org_img_url_sp = org_img_url.split("/")
    img_file = org_img_url_sp[len(org_img_url_sp)-1]
    #localfilename = "{}/{}".format(save_path,img_file)
    localfilename = os.path.join(save_path,img_file)
    if os.path.exists(localfilename) == False:
        print(org_img_url,localfilename)
        try:
            urllib.request.urlretrieve(org_img_url,filename=localfilename) #下载内容图
        except Exception as e:
            print(e)
    #return "content_img/{}/{}".format(oid,img_file)
    return os.path.join("content_img",oid,img_file)

def org_str_2_time(org_time):
    org_time_sp = org_time.split(' ')
    date_str = org_time_sp[0]
    time_str = org_time_sp[1]
    #转换日期字符串
    date_str = date_str.replace('年','-')
    date_str = date_str.replace('月','-')
    date_str = date_str.replace('日','')
    #转换时间字符串
    if time_str[0:2] == "上午":
        time_str = time_str[2:]
        #print(time_str)
    elif time_str[0:2] == "下午":
        time_str = time_str[2:]
        time_sp = time_str.split(':')
        hour = int(time_sp[0])+8
        minu = int(time_sp[1])
        time_str = "%02d:%02d" % (hour,minu)
        #print(time_str)
    out_time_str = date_str+" "+time_str
    out_time = datetime.datetime.strptime(out_time_str,"%Y-%m-%d %H:%M")
    print(out_time)
    return out_time

#保存下载页面的信息
def get_download_info(html):
    doc = pq(html)
    hidden_content = doc(".hidden-content")
    print(hidden_content.text())
    return hidden_content.text()

#打开下载页面
def open_download_url(download_url):
    js ="window.open('%s')"%(download_url)   #打开新页签
    br.execute_script(js)
    handlers =br.window_handles      #获取当前页面的句柄
    br.switch_to.window(handlers[2])
    wait = WebDriverWait(br, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hidden-content')))
    pan_info = get_download_info(br.page_source.encode("utf-8"))
    br.close()
    br.switch_to.window(handlers[1])
    return pan_info

#保存内容页面
def save_content_data(oid,html,htmlfilename):
    doc = pq(html)
    content_html = doc(".article-content")
    img_url_list = doc('.article-content img').items()
    #print(img_url_list)
    #循环保存内容中的图片并且修改图标src到本地
    for img_url in img_url_list:
        org_img_url = img_url.attr('data-src')
        if org_img_url[0:4] == "http":
            localfilename = save_img_in_content(oid,org_img_url)
            img_url.attr('src',localfilename) #修改url地址
            img_url.attr('data-src',localfilename) #修改url地址
            img_url.attr('srcset',localfilename)
    #记录时间
    item_list = doc('.item').items()
    for item in item_list:
        org_time = item.text()
        out_time = org_str_2_time(org_time)
        out_time_str = datetime.datetime.strftime(out_time,"%Y-%m-%d %H:%M:%S")
        break #只记录时间
    #判断下载标志
    down = content_html(".down")
    download_status = 0
    if down.text() == '立即下载':
        download_status = 1
    elif down.text() == '立即购买':
        download_status = 2
    #如果可以下载则获取下载页面url
    if download_status == 1:
        download_url = down.attr('href')
        pan_info = open_download_url(download_url)
    else:
        pan_info = ''
    #更新数据库时间和下载状态
    sql = "UPDATE content_table SET time=str_to_date('%s','%%Y-%%m-%%d %%H:%%i:%%S'),download='%d',pan_info='%s' WHERE  oid = '%s'" % (out_time_str,download_status,pan_info,oid)
    print(sql)
    try:
        cursor.execute(sql)  # 执行sql语句
        db.commit()          # 执行sql语句
    except Exception as e:
        print(e)
    #保存时删除下载框
    content_html(".erphpdown-box").remove()
    content_html("style").remove()
    #保存html文件
    f = open(htmlfilename,"w",encoding='utf-8')
    f.write(content_html.html())
    f.close()

def open_content_url(oid,con_url):
    #filename = "{}/{}.html".format(html_path,oid)
    filename = os.path.join(html_path,oid+".html")
    if os.path.exists(filename):#已经存在就不执行
        return
    print("open:",con_url)
    js ="window.open('%s')"%(con_url)   #打开新页签
    br.execute_script(js)
    handlers =br.window_handles      #获取当前页面的句柄
    br.switch_to.window(handlers[1]) 
    wait = WebDriverWait(br, 10)
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'single-content')))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'article-content')))
    save_content_data(oid,br.page_source.encode("utf-8"),filename)
    br.close()
    br.switch_to.window(handlers[0]) 

#解析box中的内容
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
        con_url_sp = con_url.split("/")
        oid = con_url_sp[len(con_url_sp)-1][0:-5]   #-5 .html
        save_box_data(oid,con_title,img_url,type_text,price_text)
        open_content_url(oid,con_url)
        #break #debug

# 隐性等待，最长等30秒 等待网页加载完成
#br.implicitly_wait(30)  
# 设置窗口最大化
#br.maximize_window()
# 打开一个页面https://www.iszg.cc
url = 'https://www.iszg.cc/category/fl'
#url = 'https://www.iszg.cc/category/illusion'
br.get(url)
wait = WebDriverWait(br, 10)
#登录
web_login()
#等待页面加载
logined = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'nav-login')))
posts = wait.until(EC.presence_of_element_located((By.ID, 'posts')))
#解析页面中的boxes
parse_html_boxes(br.page_source.encode("utf-8"))
#保存到文件
#f = open("iszg.html","wb")
#f.write(br.page_source.encode("utf-8"))\

for i in range(1,2): 
    time.sleep(1)
    links=br.find_elements_by_link_text("下一页")
    link=links[0] 
    url=link.get_attribute('href')
    print(url)
    br.get(url)
    posts = wait.until(EC.presence_of_element_located((By.ID, 'posts')))
    parse_html_boxes(br.page_source.encode("utf-8"))

# 关闭窗口
handlers =br.window_handles      #获取当前页面的句柄
br.switch_to.window(handlers[0]) 
# 关闭窗口
br.close()
# 退出浏览器
br.quit()
#关闭文件
csv.close()
#关闭数据库
db.close()