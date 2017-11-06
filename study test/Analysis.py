from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://xy.dryork.cn/xinyue_manage/admin/main')

#driver.find_elements_by_name('username').send_keys('admin')
#driver.find_elements_by_name('password').send_keys('admin123')
#driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
#driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('admin123')

#driver.find_element_by_xpath('//*[@id="formid"]/fieldset/div[2]/button/span').click()

cookie = driver.get_cookies()
for cookie in driver.get_cookies():
    print ("%s" % (cookie['value']))

#driver.add_cookie({'value':'66447258191A4811245DF069B4657A0B'})
driver.add_cookie({'name':'key_aaa'})
for cookie in driver.get_cookies():
    print ("%s" % (cookie['name']))

