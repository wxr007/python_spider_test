# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import os

html_path = "E:/WorkSpace/Node/my_illusion_web/views/html"
dirs = os.listdir(html_path)

def parse_html_file(file_path):
    f = open(file_path,"r",encoding='utf-8')
    content = f.read()
    f.close()
    doc =pq(content)
    img_url_list = doc('img').items()
    for img_url in img_url_list:
        org_img_url = img_url.attr('data-src')
        new_img_url = os.path.join('content_img',org_img_url)
        print(new_img_url)
        img_url.attr('src',new_img_url) #修改url地址
        img_url.attr('data-src',new_img_url) #修改url地址
        img_url.attr('srcset',new_img_url)
    f = open(file_path,"w",encoding='utf-8')
    f.write(doc.html())
    f.close()

for file in dirs:
    file_path = os.path.join(html_path,file)
    if os.path.isfile(file_path):
        print(file_path)
        parse_html_file(file_path)
        