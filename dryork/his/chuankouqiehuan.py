#coding=utf-8 '''��ֹ����'''
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
try:
 driver.get('https://www.baidu.com')
 """a=driver.current_window_handle
 print(a)
 sleep(1)"""
 driver.find_element_by_link_text('��½').click()
 driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div/div/div/div/div/div[1]/form/p[9]/a[1]').click()
 #driver.find_element_by_link_text("����ע��").click()
 #driver.find_element_by_link_text('����ע��').click()
 """all_handle=driver.window_handles
 print(all_handle)"""

except Exception as a:
  print(a)