#案例管理
import time
import csv
from itertools import islice
def Add(driver):
    entity_reader = csv.reader(open('C:\\testing\\xy\\wpsc\\case.csv','r'))
    for row in islice(entity_reader,1,None):
      driver.refresh()
      title=row[0]
      digest=row[1]
      details=row[2]
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
      time.sleep(0.5)
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/ul/li[6]/a/span').click()
      driver.switch_to.frame('cframe')
      time.sleep(0.5)
      driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/ul/li[3]/a').click()
      time.sleep(0.5)
      driver.find_element_by_xpath('//*[@id="recommend-table"]/tbody/tr[7]/td[3]/a').click()
      driver.find_element_by_xpath('//*[@id="add-modal"]').click()
      time.sleep(0.5)
      driver.find_element_by_xpath('//*[@id="caseTitle"]').send_keys(title)
      driver.find_element_by_xpath('//*[@id="caseAbstract"]').send_keys(digest)
      driver.find_element_by_xpath('//*[@id="editor1"]').send_keys(details)
      driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
      time.sleep(0.5)
      text=driver.switch_to_alert().text
      print(text)
      driver.switch_to_alert().dismiss()


