from selenium import  webdriver
from time import sleep
import csv,os,time,requests
from logger import *
from itertools import islice

#文件操作类
class operation():
  #获取当前目录
  def get_current_path(self,file_name):
    #获取当前目录
    base_dir = os.getcwd()
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
  #读取时间
  def read_time(self):
      nowtime =time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
      return  nowtime
  #读取文件
  def read_csv(self):
    '''读取文件'''
    try:
      filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
      file_name = self.get_current_path(filename)
      dats = csv.reader(open(file_name,mode='r'))
      for user in dats:
        return user
    except Exception as a:
        return False
  #csv文件写入
  def writr_csv_file(self,list_data):
    #csv文件写入
    try:
      lines = list_data
      filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
      file_name = self.get_current_path(filename)
      with open(file_name,mode='a',newline='') as somefile:
          writer1 = csv.writer(somefile)
          writer1.writerow(lines)

    except Exception as a:
        print('写入错误',a)
  #读取管理员手机号码
  def read_phone(self,filename):
    #读取管理员手机号码
    phone = []
    filepath = self.get_current_path(filename)
    dats = csv.reader(open(filepath,mode='r'))
    for i in islice(dats,1,None):
        phone.append(i[1])
    return  phone
  #md5加密
  def getMd5(self,str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()
  #日志创建
  def loggingcreate(self):
     filename=time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.log'
     file_name = self.get_current_path(filename)
     logger=Log("zzz",file_name )
     return logger

#浏览器操作
class Browser(operation):

  def __init__(self):
      # self.chrome_options = Options()
      # self.chrome_options.add_argument("--disable-extensions")
      # self.chrome_options.add_argument("--incognito")
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()


  #判断短信数量
  def sent_number_message(self):
     password =self.getMd5('zzz@yueke!')
     url = 'http://www.ztsms.cn/balance.do'
     payload={"username":"channel","password":password}
     result = requests.post(url,data=payload)
     return result.json()

  #发送短息
  def  sent_text_message(self,phone,content):
   try:
         print('发短信')
         password = self.getMd5('zzz@yueke!')
         url = 'http://www.ztsms.cn/sendSms.do'
         for i in phone:
             payload={"username":"channel","password":password,'mobile':int(i),"content":content,
                   'productid':95533,'xh':0}
             logger.critical(self.read_time()+'发送短信内容'+str(payload))
             result = requests.post(url,data=payload)
             print(result.text)
             logger.critical(self.read_time()+'返回的的发送信息'+str(result.text))
   except Exception as errormessage:
      print(errormessage)


  def screening(self,logger):
       logger.info('筛选日期')
       self.driver.find_element_by_xpath('//*[@id="encounterDate1"]').click()
       self.driver.find_element_by_xpath('/html/body/div[13]/div[3]/table/thead/tr[1]/th[1]').click()
       self.driver.find_element_by_xpath('/html/body/div[13]/div[3]/table/tbody/tr[2]/td[1]').click()
       sleep(5)
       self.driver.find_element_by_xpath('//*[@id="searchForm"]/ul[2]/li[6]/button').click()
       logger.info('成功筛选信息')

  #登陆操作

  def login(self,logger):
         '''登陆界面'''
         # self.driver.get('http://px-taiyiyun.healthcare.taikang.com/tkh-saas-web/view/saasLogin.html')#测试地址
         logger.info('登陆后台管理界面')
         self.driver.get('https://taiyiyun.taikang.com/saas/view/saasLogin.html')#正式地址
         self.driver.find_element_by_xpath('//*[@id="loginform"]/div[1]/div/div/input').send_keys('bbykyzkj0')
         logger.info('输入登陆用户名 bbykyzkj0 ')
         self.driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div/div/input').send_keys('bbykyzkj1234')
         logger.info('输入登陆用户名 输入登陆密码 ')
         self.driver.find_element_by_xpath('/''/*[@id="checkBtn"]').click()
         sleep(5)



  #获取列表并将页面中的列表数据写入csv文件
  def list_data_get(self,logger):
     #将页面中的列表数据写入csv文件
     logger.info('开始获取界面表格信息，并将信息洗写入表格')
     self.screening(logger)
     self.list_data_loc = ('//*[@id="content"]/div/div[2]/div/div/div/table')#定位列表对象
     self.list_tr_object_loc = ('tr')#行对象
     self.list_td_object_loc = ('td')#列对象
     sleep(5)
     # self.driver.find_element_by_xpath('//*[@id="top1_side17"]/span[1]').click()
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
  def get_table_phone(self,logger):
      try:
        self.screening(logger)
        new_phone = self.driver.find_element_by_xpath('//*[@id="appList"]/tr[1]/td[4]').text
        return new_phone
      except Exception as a:
         print(a)
         self.list_data_get(logger)
  #手机号码判断
  def is_phone(self,phone,logger):
     '''判断手机号码'''
     try:
        old_phone =self.read_csv()[3]
        logger.info('获取表格中的手机号码'+str(old_phone))
     except Exception as a:
         print(a)
         logger.debug(self.read_time()+'读取表格错误')
         self.list_data_get()
         old_phone =self.read_csv()[3]
         logger.info('重新获取表格中的手机号码'+str(old_phone))
     if old_phone:
        new_phone = phone
        logger.warning('当前页面手机号码的手机号码'+str(new_phone))
        print('***********正常运行*************')
        if old_phone == new_phone:
               logger.info('用户判断，当前没有新的患者信息')
        elif old_phone == None or new_phone == None:
               logger.debug('手机号码为空')
        else:
               self.driver.refresh()
               self.screening(logger)
               logger.critical(str(self.read_time())+'存在新的患者')
               #发短信操作
               phone = self.read_phone('管理员信息配置.csv')
               logger.critical(str(self.read_time())+'管理员手机号码'+str(phone))
               content = '您好，您有saas管理平台中最新患者信息请登陆后台处理需要处理【约客牙医】'
               # self.sent_text_message(phone,content)
               logger.info('剩余短信信息'+self.sent_number_message())
               logger.warning(str(self.read_time())+'剩余短信数量'+str(self.sent_number_message()))

               #将新的患者数据写入表格
               self.delete_file()
               self.list_data_get()
     else:
         self.list_data_get()

  #定时任务
  def printtime(self,logger):

    while True:
        new_phone = self.get_table_phone(logger)
        self.is_phone(new_phone,logger)
        logging.warning(self.read_time()+'判断结束')
        self.printtime
        time.sleep(300)

#主程序
def main():

    br = Browser()
    logger = br.loggingcreate()
    logger.debug('22131321313212313132')
    br.login(logger)
    sleep(3)
    br.list_data_get(logger)
    br.printtime(logger)



if __name__ == '__main__':
    main()
