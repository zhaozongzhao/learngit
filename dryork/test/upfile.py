from selenium import webdriver
import time
import os

driver=webdriver.Chrome()
driver.implicitly_wait(10)
file='file:///'+os.path.abspath('new2.html')
driver.get(file)
try:
 driver.find_element_by_xpath('/html/body/div/div/input').send_keys('C:/testing/new1.html')
except Exception as a:
 print(a)
