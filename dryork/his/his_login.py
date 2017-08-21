#coding =utf-8 '''防止乱码'''

from selenium import webdriver
from time  import sleep
from employee import employee
driver=webdriver.Chrome()
driver.get("http://60.205.149.236:8082/enjoyhisjt/admin/login.htm")
sleep(0.5)
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('86000000000')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('111111')
sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button').click()
print('登陆成功')

def  chuzhxiang2(driver):#二级处置项添加
  driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li/ul/li[1]/a/span').click()
  sleep(0.5)
  url=driver.current_url
  print(url)


  driver.switch_to.frame("cframe")#表单切换

  driver.find_element_by_id('add-modal').click()

  driver.find_element_by_xpath('//*[@id="itemCode"]').send_keys('00008')

  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[2]/div/input').send_keys('测试处置项05')

  chuzhi=driver.find_element_by_xpath('//*[@id="parentId"]')

  chuzhi.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[3]/div/select/option[3]').click()

  driver.find_element_by_xpath('//*[@id="hiscode"]').send_keys('00001')

  driver.find_element_by_xpath('//*[@id="btn_submit"]').click()

  i=driver.switch_to_alert().text

  print(i)

  #driver.switch_to_alert().accept()#接受现有警告框

  driver.switch_to_alert().dismiss()
 
def chuzhixiang3(driver):
 
  driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li/ul/li[2]/a/span').click()
  
  sleep(0.5)
  url=driver.current_url
  print(url)
  
  sleep(2)
  
  driver.switch_to.frame('cframe')#表单切换
  
  driver.find_element_by_xpath('//*[@id="add-modal"]').click()
  
  driver.find_element_by_xpath('//*[@id="itemCode"]').send_keys('00002')
  
  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[2]/div/input').send_keys('三级处置项002')
  
  i=driver.find_element_by_xpath('//*[@id="parentId"]')
  
  i.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[3]/div/select/option[3]').click()
  
  b=driver.find_element_by_xpath('//*[@id="sonId"]')
  
  b.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[4]/div/select/option[3]').click()
  
  driver.find_element_by_xpath('//*[@id="level"]').send_keys('3')
  
  driver.find_element_by_xpath('//*[@id="jtPrice"]').send_keys('100')
  
  driver.find_element_by_xpath('//*[@id="unit"]').send_keys("00001")
  
  a=driver.find_element_by_xpath('//*[@id="city"]')

  a.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[9]/div/select/option[2]').click()
  
  driver.find_element_by_xpath('//*[@id="4"]').click()  
  
  driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
  
  c=driver.switch_to_alert().text

  print(c)

  driver.switch_to_alert().accept()#接受现有警告框

  #driver.switch_to_alert().dismiss()
  

employee(driver,'测试test',111111,1000000001)
  
  
  
  
  
  
  

