import csv,os
import requests
from itertools import islice
import time

def get_current_path(file_name):
    #获取当前目录
    base_dir = os.getcwd()
    base_dir = str(base_dir)
    #将路径中的\\用\取代
    base = base_dir.replace('\\','/')
    file_path = base +'/data/'+file_name
    return  file_path


#读取管理员手机号码
def read_csv(filename):
    #读取管理员手机号码
    phone = []
    filepath = get_current_path(filename)
    dats = csv.reader(open(filepath,mode='r'))
    for i in islice(dats,1,None):
        phone.append(i[1])
    return  phone

#md5加密
def getMd5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()


#判断短信数量
def sent_number_message():
   password = getMd5('zzz@yueke!')
   url = 'http://www.ztsms.cn/balance.do'
   payload={"username":"channel","password":password}
   result = requests.post(url,data=payload)
   return result.json()

#发送短息
def  sent_text_message(phone,content):
   try:
         password = getMd5('zzz@yueke!')
         url = 'http://www.ztsms.cn/sendSms.do'
         for i in phone:
             payload={"username":"channel","password":password,'mobile':int(i),"content":content,
                   'productid':95533,'xh':0}
             print(payload)
             # result = requests.post(url,data=payload)
             # print(result.text)
   except Exception as errormessage:
      print(errormessage)



def main():
   phone = read_csv('管理员信息配置.csv')
   content = '您好，您有最新患者信息需要处理【约客牙医】'
   sent_text_message(phone,content)
   print(sent_number_message())


if __name__ == '__main__':
   main()