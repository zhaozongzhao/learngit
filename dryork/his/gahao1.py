#coding =utf-8 '''防止乱码'''

from selenium import webdriver #导入webdriver包
import os #导入os包
from time import sleep  #导入time包
chromebrowser="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"#chrome浏览器驱动
#os.environ["webdriver.chrome.browser"]=chromebrowser
browser = webdriver.Chrome(chromebrowser)
#将对象"Chrome(chromebrowser)"赋值给browser
browser.get("http://101.201.78.244:8080/enjoyhisfy/admin/login.htm")
#print("400*800")
#browser.set_window_size(480,800)
sleep(0.3)  #休眠0.3秒
browser.find_element_by_id("userid").send_keys("11111111")
sleep(0.3) 
browser.find_element_by_id("userid").clear()
sleep(0.3) 
browser.find_element_by_id("userid").send_keys("86000000000")
browser.find_element_by_id("userpassid").send_keys("111111")
#休眠0.3秒
browser.find_element_by_xpath("/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button/span").submit()

'''
test2 = webdriver.Chrome(chromebrowser)
test2.get("http://101.201.78.244:8080/enjoyhisfy/client/register/register_view.htm")
test2.refresh()

test2.find_element_by_xpath('//*[@id="patName"]').send_keys('挂号单5')
sleep(0.3)  #休眠0.3秒

test2.find_element_by_xpath("//*[@id='mobile']").send_keys('18301565568')
sleep(0.3)  #休眠0.3秒
#性别
m=test2.find_element_by_xpath("//*[@id='userSex']")
m.find_element_by_xpath("/html/body/div[1]/div/div/form/div[1]/div[2]/div/div/select/option[1]").click()
sleep(0.3)  #休眠0.3秒

#性别
n=test2.find_element_by_xpath("//*[@id='source']")
n.find_element_by_xpath("/html/body/div[1]/div/div/form/div[2]/div[2]/div/div/div[1]/select/option[2]").click()
sleep(0.3)  #休眠0.3秒
#就诊医生
i=test2.find_element_by_xpath('//*[@id="dentistId"]')
i.find_element_by_xpath("/html/body/div[1]/div/div/form/div[2]/div[3]/div/div/select/option[2]").click()
sleep(0.3)  #休眠0.3秒
#就诊科室
a=test2.find_element_by_xpath('//*[@id="deptCode"]')
a.find_element_by_xpath("/html/body/div[1]/div/div/form/div[3]/div[3]/div/div/select/option[2]").click()
sleep(0.3)  #休眠0.3秒
#就诊目的
test2.find_element_by_xpath('//*[@id="item2"]').click()
test2.find_element_by_xpath('//*[@id="add-btn"]').click()'''



'''print("返回")
browser.back()
sleep(2)
print("前进")
browser.forward()
sleep(2)

browser.refresh()
sleep(2)
browser.quit()'''
