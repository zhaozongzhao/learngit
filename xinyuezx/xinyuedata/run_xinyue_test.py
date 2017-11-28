from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import unittest
import os
import time

#===================================邮件发送======================================
def send_mail(file):
    #******************地址设置*******************************
     #发件地址
    _user = "2206321864@qq.com"
      #服务器设置地址
    _pwd = "kzdxkjuavfjbebhh"
       #接收邮箱地址
    _to   = "3031371046@qq.com"
    print(file)
    send_file=open(file,'rb').read()
    print(send_file)
    att = MIMEText(send_file,'base64','utf-8')
    att['Content-type']='application/octet-stream'
    #filename=1.htmlf附件名称
    att['Content-Disposition']='attachment; filename=xinyuezx.html'
    msg=MIMEMultipart(_to)
    #邮箱正文
    msg["Subject"] = "自动化测试报告"
    msg.attach(att)
    #邮箱地址主题
    msg["From"]    = _user#发件地址
    msg["To"]      = _to#收件地址
    try:
      s =smtplib.SMTP_SSL("smtp.qq.com", 465)
      #邮件服务器地址 端口465
      s.login(_user, _pwd)
      #登录服务器的用户名 密码
      s.sendmail(_user, _to, msg.as_string())
      #发送的信息
      s.quit()
      print ("Success!")
    except smtplib.SMTPException as e:
      print ("Falied,%s"%e )


def new_report(testreport):
    # #定义文件目录
    # result_dir = 'C:\\report'
    #os.listdir 获取目录下所有文件及文件夹
    list = os.listdir(testreport)
    list.sort(key=lambda fn: os.path.getatime(testreport+'\\'+fn))
    print(('最新文件为：'+list[-1]))
    file=os.path.join(testreport ,list[-1])
    print(file)
    return file



def runner():
    #运行文件夹绝对不要用test开始
     #discover=找到指定目录下所有的测试模块，并可递归查到子文件下的测试模块

     now=time.strftime('%Y-%m-%d %H-%m-%M')
     filename='C:\\Users\\zzz\\learngit\\xinyuezx\\xinyuedata\\report\\'+now+'resul.html'
     fp = open(filename,'wb')
     runner = HTMLTestRunner(
         stream=fp,
         title='心悦后台自动化测试报告',
         description='环境: win7 浏览器 ：chome '
     )
     discover = unittest.defaultTestLoader.discover('C:\\Users\\zzz\\learngit\\xinyuezx\\xinyuedata\\test_case',pattern = '*_sta.py')
     runner.run(discover)
     fp.close()
     file_path = new_report('C:\\Users\\zzz\\learngit\\xinyuezx\\xinyuedata\\report')#查找新生成的报告
     print(file_path)
     send_mail(file_path)#调用邮件发送功能





if __name__ == '__main__':
    runner()