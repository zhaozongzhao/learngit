import unittest
from selenium import  webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://hj.dryork.cn/huijia/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()

def minute(driver,name):
    driver.switch_to.frame('cframe')
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[10]/a').click()
    n='C:\\csv1'+'患者详情'+'.jgp'
    driver.get_screenshot_as_file(n)
    driver.find_element_by_name('标签2').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[13]/div[2]/div').click()

minute(driver,'由国娟')