#知识库（系统管理）
import random
import time
import csv
from selenium import webdriver
from itertools import islice
from selenium.webdriver.common.action_chains import ActionChains
def repositoryAdd(driver,f):
  form1=csv.reader(open('C:\\testing\\yk\wps\\repository.csv','r'))
  f.write('\n知识库添加\n')
  for x in islice(form1,1,None):
    Title=x[0]
    project=x[1]
    summary=x[2]
    Content=x[3]
    driver.refresh()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a').click()
    driver.switch_to.frame("cframe")#表单切
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="add-modal"]').click()
    time.sleep(3)
    '''h=random.randint(1, 10)
    b=random.choice('abcdefg&#%^*f')
    k='%d'%h+b'''
    driver.find_element_by_xpath('//*[@id="title"]').send_keys(Title)
    type=driver.find_element_by_xpath('//*[@id="select-zltype"]')
    type.find_element_by_xpath('%s'%project).click()
    driver.find_element_by_xpath('//*[@id="imgFile"]').send_keys('c:/testing/1.jpg')
    driver.find_element_by_xpath('//*[@id="digest"]').send_keys(summary)
    driver.find_element_by_xpath('//*[@id="editor1"]').send_keys(Content)
    driver.find_element_by_xpath('//*[@id="add-docflup-btn"]').click()
    #driver.switch_to_alert().send_keys(keysToSend)
    time.sleep(3)
    message=driver.switch_to_alert().text
    driver.switch_to_alert().dismiss()
    if message=='操作成功！':
      f.write('知识库添加成功' + '\t')
    else:
      f.write('知识库添加失败' + '\t')
#删除知识库数据
def repositoryDelete(driver,f):
  driver.find_element_by_xpath('//*[@id="menuDemo"]/li[1]/ul/li[1]/a/span').click()
  driver.switch_to.frame('cframe')
  time.sleep(0.5)
 #driver.find_element_by_xpath('//*[@id="docknowledge-table"]/tbody/tr[2]/td[4]/div/a[1]/i').click()
  #driver.find_element_css_selector('html body div.page-content div.row div.col-xs-12 div div#docadvice-table_wrapper.dataTables_wrapper.no-footer table#docadvice-table.table.table-striped.table-bordered.table-hover.dataTable.no-footer tbody tr.odd td div.hidden-sm.hidden-xs.action-buttons a.red i.ace-icon.fa.fa-trash-o.bigger-130')
  driver.find_element_by_xpath("//table[@id='docadvice-table']/tbody/tr[2]/td[8]/div/a/i").click()
  driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]').click()

def repositoryupder(driver,f):
  # click | link=医嘱管理 |
   driver.find_element_by_link_text(u"医嘱管理").click()
   driver.switch_to.frame("cframe")#表单切
   time.sleep(2)
   driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/div/table/thead/tr/th[8]').text
   double_click=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[3]/div/table/tbody/tr[1]/td[8]/div/a[2]/span')
   time.sleep(2)
   ActionChains(driver).double_click(double_click).perform()#使用鼠标定位修改按钮
   driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div/input').clear()
   driver.find_element_by_xpath('//*[@id="title"]').send_keys('医嘱_标题')
   driver.find_element_by_xpath('//*[@id="docName"]').clear()
   driver.find_element_by_xpath('//*[@id="docName"]').send_keys('医生名称和职称')
   hh=driver.find_element_by_xpath('//*[@id="select-zltype"]')
   hh.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[2]/form/div[3]/div/select/option[2]').click()
   driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
   driver.switch_to_alert().accept()#接受显示的信息