#医生管理
# coding: utf-8
from time  import sleep
import csv
from itertools import islice
def Add(driver,f):#添加
    form=csv.reader(open('C:\\testing\\xy\\wpsc\\doctor.csv','r'))
    driver.implicitly_wait(10)
    f.write('\n医生管理 添加\t')
    url=driver.current_url
    f.write(url+'\n')
    for table in islice(form,1,None):
       driver.refresh()
       mobile=table[0]
       name=table[1]
       Title=table[3]
       School=table[6]
       School1=table[7]
       brief=table[8]
       f.write(mobile+'\t'+name+'\t'+Title+'\t'+School+'\n')
       driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/a/span').click()
       driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/ul/li/a/span').click()
       driver.switch_to.frame("cframe")
       driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[1]/a').click()
       sleep(3)
       driver.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[1]/div/input').send_keys(mobile)#手机号
       driver.find_element_by_xpath('//*[@id="usernames"]').send_keys(name)#医生姓名
       driver.find_element_by_xpath('//*[@id="icon"]').send_keys('C:/testing/1.jpg')
       title=driver.find_element_by_xpath('//*[@id="titlename"]')
       title.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[4]/div/select/option[4]').click()#职称
       province=driver.find_element_by_xpath('//*[@id="province"]')
       province.find_element_by_xpath("/html/body/div[3]/div/div/div/form/div[5]/div[1]/select/option[7]").click()
       city=driver.find_element_by_xpath('//*[@id="city"]')
       city.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[5]/div[2]/select/option[1]').click()
       driver.find_element_by_xpath('//*[@id="hospId"]').send_keys(School)#任职院区
       year=driver.find_element_by_xpath('//*[@id="sel_year"]')
       year.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[7]/div[1]/select/option[2]').click()
       month=driver.find_element_by_xpath('//*[@id="sel_month"]')
       month.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[7]/div[2]/select/option[2]').click()
       day=driver.find_element_by_xpath('//*[@id="sel_day"]')
       day.find_element_by_xpath('/html/body/div[3]/div/div/div/form/div[7]/div[3]/select/option[2]').click()
       driver.find_element_by_xpath('//*[@id="graduateSchool"]').send_keys(School1)#毕业院区
       driver.find_element_by_id('s1').click()#擅长专业
       #driver.find_element_by_id('s2').click()
       #driver.find_element_by_id('s3').click()
       driver.find_element_by_xpath('//*[@id="resume"]').send_keys(brief)#简介
       driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
       sleep(2)
       test=driver.switch_to_alert().text
       f.write('\n'+test+'\n')
       driver.switch_to_alert().dismiss()
def Upder(driver,f):#修改
    f.write('\n医生管理 修改\t')
    url=driver.current_url
    f.write(url+'\n')
    driver.implicitly_wait(10)
    driver.refresh()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/a/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/ul/li/a/span').click()
    driver.switch_to.frame("cframe")
    h=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]').text
    f.write('\t'+h+'\t')
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[9]/a[2]').click()
    driver.get_screenshot_as_file('C:\\testing\\xy\\wpsc\\修改前+.jgp')
    sleep(3)
    driver.find_element_by_xpath('//*[@id="usernames"]').send_keys('修改医生姓名')
    sleep(3)
    #driver.find_element_by_id('s1').click()
    driver.find_element_by_id('s2').click()
    #driver.find_element_by_id('s3').click()
    sleep(3)
    driver.get_screenshot_as_file('C:\\testing\\xy\\wpsc\\修改后1+.jgp')
    driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
    sleep(2)
    test=driver.switch_to_alert().text
    f.write(test+'\n')
    driver.switch_to_alert().dismiss()
def Query(driver):#查询
    driver.refresh()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/a/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[4]/ul/li/a/span').click()
    driver.switch_to.frame("cframe")
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('赵')
    #driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[4]').send_keys('')
    type=driver.find_element_by_xpath('//*[@id="certMore"]')
    type.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/select/option[3]').click()
    driver.find_element_by_xpath('//*[@id="commitSearch"]').click()
    sleep(3)
    driver.get_screenshot_as_file('C:\\pictore\\查询+.jgp')
    h=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]').text
    print(h)



