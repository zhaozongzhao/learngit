#coding =utf-8 '''防止乱码'''

from selenium import webdriver #导入webdriver包
import os #导入os包
from time import sleep  #导入time包
from selenium.webdriver.common.action_chains import ActionChains#导入鼠标驱动的类actionchains
chromebrowser="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"#chrome浏览器驱动
#os.environ["webdriver.chrome.browser"]=chromebrowser
browser= webdriver.Chrome(chromebrowser)
#将对象"Chrome(chromebrowser)"赋值给browser
url='http://101.201.78.244:8080/enjoyhisfy/admin/login.htm'
print("访问地址%s" %(url))
browser.get(url)
print(browser.title)
#print("400*800")
#browser.set_window_size(480,800)

print ("浏览器最大化")
browser.maximize_window()  #将浏览器最大化显示
sleep(2)
size=browser.find_element_by_id("userid").size#获得输入框的尺寸
print(size)
browser.find_element_by_id("userid").send_keys("11111111")
text=browser.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div[1]/div/div/h4/i").text#获得输入框的尺寸"""
print(text)
sleep(0.3)  #休眠0.3秒 
browser.find_element_by_id("userid").clear()
sleep(0.3) 
browser.find_element_by_id("userid").send_keys("86000000000")
browser.find_element_by_id("userpassid").send_keys("111111")
browser.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button/span").submit()
#休眠0.3秒
right_click=browser.find_element_by_xpath("/html/body/div[2]/div[1]/ul/li/ul/li[1]/a/span")#定位要右击得元素
ActionChains(browser).context_click(right_click).perform()#对定位元素执行鼠标右击操作


