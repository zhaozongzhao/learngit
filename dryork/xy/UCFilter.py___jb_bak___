from time import sleep
def Title(driver):
     for n in range(1,11):
       url='/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[2]'
       sleep(0.3)
       test=driver.find_element_by_xpath(url).text
       print(test)
       if test=='精神分裂症（测试）':
         sleep(5)
         test=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[5]/a[1]').text
         driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr['+str(n)+']/td[5]/a[1]').click()
         print(test)
         sleep(3)
         '''test1=driver.switch_to_alert().text
         print(test1)'''
         driver.switch_to_alert().dismiss()
         break
       elif n==10:
         sleep(0.5)
         driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/ul/li[3]/a').click()
         Title(driver)
