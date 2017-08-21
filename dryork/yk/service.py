#多点执业
def service(driver):
 try:
   import random
   import time
   print("进入多点执业界面")
   driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
   time.sleep(1)
   driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/ul/li[3]/a/span').click()
   driver.switch_to.frame("cframe")#表单切
   time.sleep(3)
   h=random.randint(1, 10)
   b=random.choice('abcdefg&#%^*f')
   k='%d'%h+b
   i=0
   mod=18301565568
   while i<10:
     time.sleep(0.5)
     driver.find_element_by_xpath('//*[@id="add-modal"]').click()
     time.sleep(1)
     driver.find_element_by_xpath('//*[@id="userName"]').send_keys('测试'+k+'号')
     driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
     driver.find_element_by_xpath('//*[@id="nickname"]').send_keys('测试'+k+'号')
     mod=18301565568
     driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(mod)
     driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
     time.sleep(1)
     message=driver.switch_to_alert().text
     print(message)
     driver.switch_to_alert().accept()
     mod=mod+1
     i=i+1
 except Exception as e:
   print(e)
 else:
   print('添加成功')
 finally:
   print('')





