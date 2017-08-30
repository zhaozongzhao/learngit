import unittest#患者管理评估报告
from selenium import  webdriver
import time
import os
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://hj.dryork.cn/huijia/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()



def checkadd(driver):
    driver.switch_to_frame('cframe')
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[11]/a').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="melupdate"]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div/div[1]/div/div/div[2]/button').click()
    time.sleep(0.5)
    #截图查看应版本问题截图暂不好用
    #n='C:\\csv1'+'患者详情'+'.jgp'
    #driver.get_screenshot_as_file(n)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div/div[1]/div/div/div[2]/div[3]/div[1]/div/button').click()
    time.sleep(2)
    os.system('F:\\3.exe')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div/div[1]/div/div/div[2]/div[5]/div[2]/div/button').click()
     #截图查看应版本问题截图暂不好用
    #n='C:\\csv1'+'患者详情'+'.jgp'
    #driver.get_screenshot_as_file(n)


checkadd(driver)