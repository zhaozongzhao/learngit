#资讯管理
def add(driver,f):
   # try:
        import time
        f.write('添加资讯\t')
        i=12
        while i<=22:
         driver.refresh()
         driver.find_element_by_xpath('//*[@id="menuDemo"]/li[2]/a').click()
         driver.find_element_by_xpath('//*[@id="menuDemo"]/li[2]/ul/li[2]/a').click()
         driver.switch_to.frame("cframe")
         time.sleep(0.5)
         driver.find_element_by_xpath('//*[@id="add-modal"]').click()
         time.sleep(0.5)
         h=driver.find_element_by_xpath('//*[@id="diseaseId"]')
         time.sleep(0.5)
         h.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[1]/div/select/option[25]').click()
         time.sleep(0.5)
         driver.find_element_by_xpath('//*[@id="info-modal-form"]/div[2]/div/input').send_keys('C:/testing/1.jpg')
         time.sleep(0.5)
         driver.find_element_by_xpath('//*[@id="title"]').send_keys('参赛'+'%s'%i)
         driver.find_element_by_xpath('//*[@id="abstracts"]').send_keys('摘要')
         driver.find_element_by_xpath('//*[@id="editor1"]').send_keys('数据')
         time.sleep(0.5)
         driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
         time.sleep(2)
         driver.switch_to_alert().dismiss()
         i=i+1
    #except Exception as a:
      #  print(a)
    #else:
      # print('添加成功')