from selenium import webdriver
import time

# 获取一个浏览器对象
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--user-data-dir=C:\\Users\\zhangchen\\AppData\\Local\\Google\\Chrome\\User') #设置成用户自己的数据目录
br = webdriver.Chrome(chrome_options=chrome_options)

# 打开一个页面
br.get('http://www.baidu.com')

# 获取页面的源代码（运行后在内存中渲染的页面元素）
#print(br.page_source)
time.sleep(1)
# 根据id查找元素
kw = br.find_element_by_id('kw')
# 往表单输入框中输入内容
kw.send_keys('python')
# 点击某个元素
br.find_element_by_id('su').click()

time.sleep(1)

# 设置窗口最大化
br.maximize_window()
time.sleep(2)

# 将页面内容保存成截图
br.save_screenshot('./1.png')
# 指定浏览器窗口大小
br.set_window_size(1200, 800)

# 设置浏览器的坐标 四个参数分别是 x坐标 y坐标 窗口的宽 框框的高
br.set_window_rect(100, 200, 300, 500)

# 获取所有cookie
print(br.get_cookies())
print('*' * 10)
# 获取某一个cookie的信息
print(br.get_cookie('BDORZ'))


time.sleep(2)
# 关闭窗口
br.close()
# 退出浏览器
time.sleep(2)
br.quit()