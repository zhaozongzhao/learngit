#coding=utf-8
from appium import  webdriver
from time import sleep
from appium.webdriver.mobilecommand import MobileCommand
import login
import swipe
import Card
import order
import news
#导入需要支持的包
def Driver():
  desired_caps = {}
  desired_caps['platformName'] = 'Android'
  desired_caps['platformVersion'] = '5.1.1'
  desired_caps['deviceName'] = 'Android Emulator'
  desired_caps["unicodeKeyboard"] = "True"#appium中文输入
  desired_caps["resetKeyboard"] = "True"#appium中文输入
  #desired_caps['app']='F:/约克app/产品迭代/dryork.apk'
  desired_caps['appPackage'] = 'com.dentist.android'
  desired_caps['appActivity'] = '.ui.WelcomeActivity'
  #输入键对值字典
  driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
   #代码与appium建立连接
  return driver
driver=Driver()
sleep(5)
news.text(driver)



