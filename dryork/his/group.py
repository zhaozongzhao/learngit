from selenium import webdriver
import os#打开本地文件需要od模块
from time import sleep
driver=webdriver.Chrome()
file1='file:///'+os.path.abspath('new1.html')#path.abspath 打开当前路径下文件，脚本与文件放在同一目录
driver.get(file1)

#inputs=driver.find_elements_by_tag_name('input')#选择页面上所有tag_name为input的元素
#inputs=driver.find_elements_by_xpath("//input[@type='checkbox']")
inputs=driver.find_elements_by_css_selector("input[type='checkbox']")                                                                          
for i in inputs:
  if i.get_attribute("type"):
    i.click()
    sleep(1)

print(len(inputs))
driver.find_elements_by_css_selector("input[type='checkbox']").pop(0).click()
sleep(1)

driver.quit() 