from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
user=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/a[7]").text
print(user)
url=driver.current_url
print(url)
title=driver.title
print(title)
"""#悬停
xuanting=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[8]')
ActionChains(driver).move_to_element(xuanting).perform()
sleep(2)"""
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/a[6]').click()
print("进入后")
user=driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/form/span[1]/a').text
print(user)
url=driver.current_url
print(url)
title=driver.title
print(title)

"""#定位到要双击的元素
qqq =driver.find_element_by_xpath("xxx")
#对定位到的元素执行鼠标双击操作
ActionChains(driver).double_click(qqq).perform()"""

"""#定位元素的原位置
element = driver.find_element_by_name("source")
#定位元素要移动到的目标位置
target =  driver.find_element_by_name("target")

#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()"""

 
