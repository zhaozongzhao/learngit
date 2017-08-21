def employee (driver,a,b,mob):
 try:
  driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li/ul/li[3]/a/span').click()
  driver.switch_to.frame("cframe")#表单切
  driver.find_element_by_xpath('//*[@id="employeeName"]').send_keys('孙乃鹤')
  driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/div/button').click()
  driver.find_element_by_xpath('//*[@id="add-modal"]').click()
  driver.find_element_by_xpath('//*[@id="employeeName2"]').send_keys(a)
  driver.find_element_by_xpath('//*[@id="password"]').send_keys(b)
  driver.find_element_by_xpath('//*[@id="mobile1"]').send_keys(mob)
  i=driver.find_element_by_xpath('//*[@id="userType"]')
  i.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[4]/div/select/option[5]').click()
  user=driver.find_element_by_xpath('//*[@id="roleId"]')
  user.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[5]/div/select/option[2]').click()
  unit=driver.find_element_by_xpath('//*[@id="unitCode1"]')
  unit.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[6]/div/select/option[2]').click()
  k=driver.find_element_by_xpath('//*[@id="departId"]')
  k.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div/form/div[7]/div/select/option[5]').click()
  driver.find_element_by_xpath('//*[@id="discRate"]').send_keys('60')
  driver.find_element_by_xpath('//*[@id="title"]').send_keys('教授')
  driver.find_element_by_xpath('//*[@id="optionsRadios1"]').click()
  driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
  c=driver.switch_to_alert().text
  print(c)
  driver.switch_to_alert().dismiss()
 except Exception as e:
  print(e)
 finally:
  print('执行结束')

 
 