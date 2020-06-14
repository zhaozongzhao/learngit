import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


# 邮件发送
def mail(file, file1):
    _user = "2206321864@qq.com"
    # 发件地址
    _pwd = "kzdxkjuavfjbebhh"
    # 服务器设置地址
    _to = "3031371046@qq.com"
    # 接收邮箱地址

    sendfile = open(file, 'rb').read()
    # msg = MIMEText('这是一个测试文案')
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename=1.html'
    # filename=1.htmlf附件名称

    msg = MIMEMultipart(_to)
    # 邮箱正文
    msg["Subject"] = "don't panic"
    msg.attach(att)
    # 邮箱地址主题
    msg["From"] = _user  # 发件地址
    msg["To"] = _to  # 收件地址

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 邮件服务器地址 端口465
        s.login(_user, _pwd)
        # 登录服务器的用户名 密码
        s.sendmail(_user, _to, msg.as_string())
        # 发送的信息
        s.quit()
        print("Success!")
    except smtplib.SMTPException as e:
        print("Falied,%s" % e)


def find_file():
    # 定义文件目录
    result_dir = 'C:\\report'

    # os.listdir 获取目录下所有文件及文件夹
    list = os.listdir(result_dir)

    list.sort(key=lambda fn: os.path.getatime(result_dir + '\\' + fn))

    print(('最新文件为：' + list[-1]))

    file = os.path.join(result_dir, list[-1])

    return file, list[-1]


def runner():
    # 运行文件夹绝对不要用test开始
    # discover=找到指定目录下所有的测试模块，并可递归查到子文件下的测试模块
    test_huijia = 'C:\\Users\\zzz\\learngit\\test_CheckDoctor'

    report_dir = 'C:\\report'

    discover = unittest.defaultTestLoader.discover(test_huijia, pattern='test*py')  # 要测试模块的目录，用例文件名的匹配原则

    now = time.strftime('%Y-%m-%d %H-%m-%M')

    filename = report_dir + '\\' + now + "result.html"  # 定位报告用例存放位置

    fp = open(filename, 'wb')
    #
    runner = HTMLTestRunner(stream=fp, title='测试报告', description=u'用例执行情况:')
    runner.run(discover)
    fp.close()
    file = find_file()
    mail(file[0], file[1])


runner()
