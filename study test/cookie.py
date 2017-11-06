
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie= driver.get_cookies()



#向cookies中的name和value中添加数据
driver.add_cookie({'name':'key_aaa','value':'value-bbb'})

#遍历cookie中的name和vale信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print ("%s -> %s" % (cookie['name'], cookie['value']))


#将获得cookie的信息打印
#print (cookie)

#两种删除cookie的方法

# 删除一个特定的cookie
driver.delete_cookie('CookieName')

# 删除所有cookie
driver.delete_all_cookies()





driver.close()