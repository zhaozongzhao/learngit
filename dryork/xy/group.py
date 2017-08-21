
#医生集团
from time import sleep
import csv
from itertools import islice
def Add(driver,f):
    table=csv.reader(open('C:\\testing\\xy\\wpsc\\group.csv','r'))
    for table in islice(table,1,None):
      driver.refresh()
      name=table[0]
      user=table[1]
      username=table[2]
      introduce=table[3]
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/a/span').click()
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/ul/li/a/span').click()
      driver.switch_to.frame("cframe")
      driver.find_element_by_xpath('//*[@id="add-modal"]').click()
      sleep(0.5)
      driver.find_element_by_xpath('//*[@id="names"]').send_keys(name)#集团名称
      driver.find_element_by_xpath('//*[@id="icon"]').send_keys('C:/testing/1.jpg')#集团标示图
      level=driver.find_element_by_xpath('//*[@id="levels"]')
      level.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[3]/div/select/option[2]').click()
      sleep(0.5)
      province=driver.find_element_by_xpath('//*[@id="province"]')
      province.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[4]/div[1]/select/option[2]").click()
      city=driver.find_element_by_xpath('//*[@id="city"]')
      city.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[4]/div[2]/select/option').click()
      driver.find_element_by_xpath('//*[@id="creatorIds"]').send_keys(user)
      driver.find_element_by_xpath('//*[@id="creators"]').send_keys(username)
      driver.find_element_by_id('s1').click()#擅长专业
      driver.find_element_by_id('s2').click()
      #driver.find_element_by_id('s3').click()
      driver.find_element_by_xpath('//*[@id="introduction"]').send_keys(introduce)
      driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
      sleep(3)
      test=driver.switch_to_alert().text
      print(test)
      driver.switch_to_alert().dismiss()
def examine(driver):
    driver.refresh()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/a/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/ul/li/a/span').click()
    driver.switch_to.frame("cframe")
    sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[8]/a[1]').click()
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="yes_cert"]').click()
    #driver.find_element_by_xpath('//*[@id="yes_certRemark"]').send_keys('审核通过')
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/div[5]/button[2]').click()
    sleep(0.5)
    test=driver.switch_to_alert().text
    print(test)
    sleep(0.5)
    driver.switch_to_alert().dismiss()
def Query(driver):
    driver.refresh()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/a/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[5]/ul/li/a/span').click()
    driver.switch_to.frame("cframe")
    driver.find_element_by_xpath('//*[@id="creator"]').send_keys('赵五')#创建者
    driver.find_element_by_xpath('//*[@id="name"]').send_keys('测试医生集团')
    level=driver.find_element_by_xpath('//*[@id="level"]')#级别
    level.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[4]/select/option[2]').click()
    state=driver.find_element_by_xpath('//*[@id="status"]')#状态
    state.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/select/option[3]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="commitSearch"]').click()
