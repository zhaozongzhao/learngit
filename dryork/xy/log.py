#心悦登录
from selenium import webdriver
from time import sleep
def log(url,csv_reader):
   import Title#添加职称
   import banner#添加图片
   import message
   import entity#添加病种
   import guide#添加指南
   import expert#添加专家团
   import site2#执业地点
   import doctor1#医生管理
   import group#医生集团
   import fund#提现金额
   import case #案例管理
   from itertools import islice#使用跳过第一行
   driver=webdriver.Chrome()
   for row in islice(csv_reader,1,None):#islice
     user=row[0]
     password=row[1]
     driver.get(url)
     f=open('c:/test.txt','w+')
     f.write('心悦医众\n')
     f.write('界面\turl\ttext\异常\talert\n')
     f.write('登陆界面'+'\t')
     url=driver.current_url
     f.write(url+'\t')
     n='C:\\testing\\xy\\wpsc\\'+'登录界面'+'.jgp'
     driver.get_screenshot_as_file(n)
     driver.find_element_by_xpath('//*[@id="userid"]').send_keys(user)
     driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys(password)
     driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button').click()
     try:
        test=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        f.write(test+'\n')
     except Exception as test:
        s='%s'%test
        f.write('\n'+s+'\n')
        sleep(0.5)
        h=driver.switch_to_alert().text
        f.write('\n'+h+'\n')
        driver.switch_to_alert().accept()
     finally:

        # try:
          ''' entity.add(driver,f)#添加病种
           entity.Delete(driver,f)#停用已经启用的病种
           Title.add(driver,f)#添加职称'''
           # banner.add(driver,f)
           #wps.jt(driver)
           #Title.add(driver,f,url,csv_reader)
           #message.add(driver,f)咨询添加

           #guide.add(driver)
           #expert.Add(driver)
           #site2.add(driver)
           #doctor1.Add(driver,f)
           #doctor1.Upder(driver,f)
           #doctor1.Query(driver)
           #group.Add(driver,f)
           #group.examine(driver)
           #group.Query(driver)查询
           #fund.audit(driver)
     case.Add(driver)

        #except Exception as a:
           # s='%s'%a
            #f.write(s)








