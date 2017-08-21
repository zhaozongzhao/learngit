#coding =utf-8 '''防止乱码'''

from selenium import webdriver #导入webdriver包
import os #导入os包
from time import sleep  #导入time包
chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"#chrome浏览器驱动
#os.environ["webdriver.chrome.browser"]=chromedriver
browser = webdriver.Chrome(chromedriver)
#将对象"Chrome(chromedriver)"赋值给browser
browser.get("http://101.201.78.244:8080/enjoyhisfy/admin/login.htm")
print("400*800")
browser.set_window_size(480,800)
sleep(0.3)  #休眠0.3秒
browser.find_element_by_id("userid").send_keys("86000000000")
browser.find_element_by_id("userpassid").send_keys("111111")
#休眠0.3秒
browser.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button/span").click()
print("返回")
browser.back()
sleep(2)
print("前进")
browser.forward()
sleep(2)

browser.refresh()
sleep(2)
browser.quit()

