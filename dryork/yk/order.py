#医嘱管理
from time import  sleep
from itertools import islice
import csv
def ADD(driver,f):
    title=csv.reader(open('C:\\testing\\yk\wps\\orderAdd.csv','r'))
    for x in islice(title,1,None):
      headline=x[0]#标题
      name=x[1]#名称
      #item=x[2]#项目
      icon=x[3]#图标
      background=x[4]#背景图
      driver.refresh()
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[2]/a/span').click()
      driver.switch_to.frame('cframe')
      sleep(0.8)
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a/span').click()
      sleep(0.5)
      driver.find_element_by_xpath('//*[@id="title"]').send_keys(headline)
      driver.find_element_by_xpath('//*[@id="docName"]').send_keys(name)
      item=driver.find_element_by_xpath('//*[@id="select-zltype"]')#所属治疗项目
      item.find_element_by_xpath('//*[@id="select-zltype"]/option[3]').click()
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/form/div[4]/div/input').send_keys(icon)#上传图标
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/form/div[5]/div/input').send_keys(background)#首屏背景图
      driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
      sleep(3)
      h=driver.switch_to_alert().text
      print('%s'%h)
      driver.switch_to_alert().dismiss()
