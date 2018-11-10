#职称管理
import csv
import time


def add(driver,f):
  test=csv.reader(open('C:\\testing\\xy\\wpsc\\test.csv','r'))
  for i in test:
     h=i[0]
     print(h)
     #log.log(url,csv_reader)
     driver.refresh()
     driver.get('http://xy.dryork.cn/dryork_xinyue_manage/admin/main')
     time.sleep(0.5)
     driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[2]/a/span').click()
     driver.switch_to.frame("cframe")
     time.sleep(0.5)
     driver.find_element_by_xpath('//*[@id="add-modal"]').click()
     time.sleep(0.5)
     driver.find_element_by_xpath('//*[@id="titlesName"]').clear()
     driver.find_element_by_xpath('//*[@id="titlesName"]').send_keys(h)
     driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
     time.sleep(0.5)
     h=driver.switch_to_alert().text
     print(h)
     time.sleep(0.5)
     driver.switch_to_alert().accept()

def Read(driver):
     driver.get('http://xy.dryork.cn/dryork_xinyue_manage/admin/main')
     time.sleep(0.5)
     driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[2]/a/span').click()
     driver.switch_to.frame("cframe")
