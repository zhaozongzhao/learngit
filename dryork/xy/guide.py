#指南管理
def add(driver):
    import csv
    from time import sleep
    from itertools import islice
    entity_reader = csv.reader(open('C:\\testing\\xy\\wpsc\\guide.csv','r'))
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/ul/li[3]/a/span').click()
    driver.switch_to.frame('cframe')
    driver.find_element_by_xpath('//*[@id="recommend-table"]/tbody/tr[1]/td[4]/a').click()
    for test in islice(entity_reader,1,None):
      name=test[0]
      duty=test[2]
      intro=test[3]
      word=test[4]
      sleep(0.5)
      driver.find_element_by_xpath('//*[@id="add-modal"]').click()
      sleep(0.5)
      driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[1]/div/input').send_keys(name)
      sleep(0.5)
      driver.find_element_by_xpath('//*[@id="iconnImg"]').send_keys('C:/testing/1.jpg')
      driver.find_element_by_xpath('//*[@id="editorTitles"]').send_keys(duty)
      driver.find_element_by_xpath('//*[@id="editorIntroduction"]').send_keys(intro)
      driver.find_element_by_xpath('//*[@id="editorMessage"]').send_keys(word)
      driver.find_element_by_xpath('//*[@id="add-guide-edit-btn"]').click()
      sleep(0.5)
      driver.switch_to_alert().dismiss()