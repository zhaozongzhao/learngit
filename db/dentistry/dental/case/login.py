from selenium import  webdriver
from time import sleep
from threading import Timer
import csv,os,time
import logging

class Browser:

  def __init__(self):
      self.driver = webdriver.Chrome()

 #获取当前目录

  #获取当前目录
  def get_current_path(self,file_name):
    #获取当前目录
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    #将路径中的\\用\取代
    base = base_dir.replace('\\','/')
    file_path = base +'/data/'+file_name
    return  file_path

  #删除文件
  def delete_file(self):
    #删除文件
    filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
    file_name = self.get_current_path(filename)
    os.remove(file_name)

  #读取文件
  def read_csv(self):
    '''读取文件'''
    filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
    file_name = self.get_current_path(filename)
    dats = csv.reader(open(file_name,encoding='utf-8',mode='r'))
    for user in dats:
        return user

  #csv文件写入
  def writr_csv_file(self,list_data):
    #csv文件写入
    try:
      lines = list_data
      filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
      file_name = self.get_current_path(filename)
      with open(file_name,mode='a',encoding='utf-8',newline='') as somefile:
          writer1 = csv.writer(somefile)
          writer1.writerow(lines)

    except Exception as a:
        print('写入错误',a)

  #***************************************************************************操作数据**********************
  #登陆操作
  def login(self):
      '''登陆界面'''
      try:
         # self.driver.get('http://px-taiyiyun.healthcare.taikang.com/tkh-saas-web/view/saasLogin.html')#测试地址
         self.driver.get('https://taiyiyun.taikang.com/saas/view/saasLogin.html')#正式地址
         self.driver.find_element_by_xpath('//*[@id="loginform"]/div[1]/div/div/input').send_keys('bbykyzkj0')
         self.driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div/div/input').send_keys('bbykyzkj1234')
         self.driver.find_element_by_xpath('//*[@id="checkBtn"]').click()
      except Exception as a:
          print('登录错误',a)

  #获取列表并将页面中的列表数据写入csv文件
  def list_data_get(self):
     #将页面中的列表数据写入csv文件
     self.list_data_loc = ('//*[@id="content"]/div/div[2]/div/div/div/table')#定位列表对象
     self.list_tr_object_loc = ('tr')#行对象
     self.list_td_object_loc = ('td')#列对象
     sleep(5)
     self.driver.find_element_by_xpath('//*[@id="top1_side17"]/span[1]').click()
     #定义获取列表数据的组
     list_data = []
     #获取列表对象
     table = self.driver.find_element_by_xpath(self.list_data_loc)
     #获取列对象
     trlist = table.find_elements_by_tag_name(self.list_tr_object_loc)
     for row  in trlist:
         tdlist = row.find_elements_by_tag_name(self.list_td_object_loc)
         for col in tdlist:
             list_data.append(col.text)
         if list_data != []:
           self.writr_csv_file(list_data)
         print(list_data)
         list_data = []


  #获取手机号码元素数据
  def get_table_phone(self):
      new_phone = self.driver.find_element_by_xpath('//*[@id="appList"]/tr[1]/td[4]').text
      return new_phone

  #手机号码判断
  def is_phone(self,phone):
     '''判断手机号码'''
     old_phone =self.read_csv()[3]
     new_phone = phone
     print(old_phone)
     print('************************')
     print(new_phone)
     if old_phone == new_phone:
         print('没有新的患者')
     elif old_phone == '' or new_phone == '':
         self.driver.refresh()
         print('手机号码获取错误')
     else:
         print('发短信')

         #将新的患者数据写入表格
         self.delete_file()
         self.list_data_get()


  def printtime(self):
    while True:
        new_phone = self.get_table_phone()
        self.is_phone(new_phone)
        self.printtime
        time.sleep(5)



def main():
    br = Browser()
    br.login()
    sleep(5)
    # br.list_data_get()
    br.printtime()



if __name__ == '__main__':
    main()
