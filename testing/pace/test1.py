#_*_conding:utf-8_*_
from appium import webdriver
from selenium.webdriver.common.by import By
import time
desired_caps={
  'platformName':'Android',#手机操作系统
  'platformVersion':'4.4.2',#系统版本
  'deviceName':'Android Emulator',#安卓这个关键字不起作用但必须要有
  'unicodekeyboard':True,
  'resetkeyboard':True,
  'app':'C:/testing/dryork.apk',#apk
  'appPackage':'com.dentist.android',
  'appActivity':'.ui.CodeLoginActivity'
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
