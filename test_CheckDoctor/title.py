from selenium import webdriver
import time
import unittest
driver=webdriver.Chrome
driver.get('http://101.201.78.244:8098/jiandaifu_manage/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('admin123')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button').click()

