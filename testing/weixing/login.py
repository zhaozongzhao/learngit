#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'ui.tools.CountryCodeU'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(0.8)
driver.find_element_by_id('com.tencent.mm:id/cdi').click()
driver.find_element_by_id('com.tencent.mm:id/brm').clear()
driver.find_element_by_id('com.tencent.mm:id/brm').send_keys('18301565568')
driver.find_element_by_id('com.tencent.mm:id/gr').send_keys('zzz284117')
driver.find_element_by_id('com.tencent.mm:id/aax').click()
sleep(3)
h=driver.switch_to_alert().text
print(h)
driver.switch_to_alert().dismiss()
