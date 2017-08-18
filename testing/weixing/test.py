#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android' #使用哪种移动平台。iOS, Android, orFirefoxOS
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '133524991618488'#启动哪种设备，是真机还是模拟器
desired_caps['appPackage'] = 'com.dentist.android'
desired_caps['appActivity'] = '.ui.CodeLoginActivity'
#/
driver = webdriver.Remote('http://localhost:21503/wd/hub', desired_caps)
#webdriver.Remote实际上就是原生webdriver的子类，另外Remote()构造函数的第一个参数中需要显示指定appium server监听的端口
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
