#coding=utf-8 '''防止乱码'''
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
try:
 driver.get('https://www.baidu.com')
 a=driver.current_window_handle
 print(a)
 sleep(1)
 driver.find_element_by_link_text('登录').click()
 sleep(3)
 driver.find_element_by_link_text('立即注册').click()
 all_handle=driver.window_handles
 print(all_handle)
 for handle in all_handle:
  if handle!=a:
   driver.switch_to.window(handle)
   print(handle)
   driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('user')
   driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys('password')
except Exception as a:
  print(a)
  
  
