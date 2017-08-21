from selenium import webdriver
from user import user
from role import role
import organization
f =open("c:/test.txt", "w+")
f.write('界面\turl\ttitle\ntext')
f.write('登陆界面'+'\t')
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://wx.dryork.cn:8081/admin/login')
url=driver.current_url
f.write(url+'\t')
title=driver.title
f.write(title+'\n')
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div/input').send_keys('admin')
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div/input').send_keys('123')
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[3]/button').click()
#user(driver)#新建用户
#role(driver)新建角色
#organization.delete(driver,f)
organization.organization(driver,f)
f.close()