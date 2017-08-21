def add(driver):
     from time import sleep
     import csv
     from itertools import islice
       #driver.implicitly_wait(30)
     driver.implicitly_wait(10)
       #静态等待
     task=csv.reader(open('C:\\testing\\yk\wps\\task.csv','r'))
     for x in islice(task,1,None):
       mold=x[0]
       Dname=x[1]
       Pname=x[2]
       driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[14]/a/span').click()
       driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[14]/ul/li/a/span').click()
       driver.switch_to.frame('cframe')
       sleep(0.5)
       driver.find_element_by_xpath('//*[@id="task-modal"]').click()
       sleep(0.5)
       type=driver.find_element_by_xpath('//*[@id="newTaskType"]')
     #任务类型1复诊提醒2随访
       a='/html/body/div[4]/div/div/div/div/div[2]/div[1]/select/option[@value="%s"]'%mold
       print(a)
       type.find_element_by_xpath('%s'%a).click()
       doctor=driver.find_element_by_xpath('//*[@id="docIDS"]')
       doctor.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[3]/div[1]/select/option[@value="114000"]').click()
       patient=driver.find_element_by_xpath('//*[@id="patid"]')
       patient.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[3]/div[2]/select/option[10]').click()
       driver.find_element_by_xpath('//*[@id="creatTime7"]').click()
       driver.find_element_by_xpath('/html/body/div[13]/div[3]/table/tbody/tr[3]/td[3]').click()
       driver.find_element_by_xpath('//*[@id="creatTime8"]').click()
       driver.find_element_by_xpath('/html/body/div[14]/div[3]/table/tbody/tr[4]/td[5]').click()
       driver.find_element_by_xpath('//*[@id="remarks"]').send_keys('这个是备注信息')
       driver.find_element_by_xpath('//*[@id="btn1men"]').click()
       driver.switch_to_alert().accept()
def daily(driver):
    from time import sleep
    i=1
    while i<=100:
     driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[14]/a/span').click()
     driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[14]/ul/li/a/span').click()
     driver.switch_to.frame('cframe')
     sleep(0.5)
     driver.find_element_by_xpath('//*[@id="report-modal"]').click()
     sleep(5)
     driver.find_element_by_xpath('//*[@id="reportMenu"]').click()
     i=i+1
     driver.switch_to_alert().accept()
     driver.refresh()

