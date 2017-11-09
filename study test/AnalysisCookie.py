from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")

time.sleep(3)
#driver.maximize_window() # 浏览器全屏显示


#通过用户名密码登陆
driver.find_element_by_id("input1").send_keys("fnngj")
driver.find_element_by_id("input2").send_keys("123456")

#勾选保存密码
#driver.find_element_by_id("remember_me").click()
#time.sleep(3)
#点击登陆按钮
driver.find_element_by_id("signin").click()

#获取cookie信息并打印
cookie= driver.get_cookies()
print(cookie)

time.sleep(2)
#driver.close()