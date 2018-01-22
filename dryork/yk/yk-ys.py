#主程序
from selenium import webdriver
from time import sleep
from login import login
import repository
import task
import order
from service import service
driver=webdriver.Chrome()
#try:
f =open("C:/test.txt", "w+")
f.write('\n\t约克医众\n ')
f.write('界面\turl\ttitle\text\n')
f.write('登陆界面'+'\t')
driver.get('http://testmange.dryork.cn/yueke/admin/main')#约克登录界面
url=driver.current_url
f.write(url+'\t')
user='admin'
password='admin123'
login(driver,user,password,f)



#repository.repositoryAdd(driver,f)#知识库添加
#repository.repositoryDelete(driver,f)#知识库修改
#repository.repositoryupder(driver,f)#知识库更新
# task.daily(driver)

#order.ADD(driver,f)
#driver.quit()
#except Exception  as a:
   # print (a)
#service(driver)

#sleep(5)
