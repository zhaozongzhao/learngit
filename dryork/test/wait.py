#coding =utf-8 '''防止乱码'''
from selenium import webdriver
#显式等待方法1
'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
#WebDriverWait检查当前页面元素是否存在
#until到返回true为止
element=WebDriverWait(driver,5,0.5).until(
 EC.presence_of_element_located((By.ID,"kw"))
 )
element.send_keys('selenium')'''
'''#显式等待方法2
from time import sleep,ctime
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

print(ctime())
for i in range(10):
 try:
  a=driver.find_element_by_id("kw")
  if a.is_displayed():#判断元素状态，状态为true,break跳出循环
    break
 except:pass
 sleep(1)
else:
 print("time out")
driver.close()
print(ctime())'''
#隐式等待

from selenium.common.exceptions import NoSuchElementException
from time import ctime
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
try:
 print(ctime())
 driver.find_element_by_id("kw1").send_keys('NoSuchElementException')
except NoSuchElementException as e:
 print(e)
finally:
 print(ctime()) 


