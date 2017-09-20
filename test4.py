import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

_user = "2206321864@qq.com"
#发件地址
_pwd  = "kzdxkjuavfjbebhh"
#服务器设置地址
_to   = "3031371046@qq.com"
#接收邮箱地址

sendfile=open('C:\\1.txt','rb').read()
#msg = MIMEText('这是一个测试文案')
att = MIMEText(sendfile,'base64','utf-8')
att['Content-type']='application/octet-stream'
att['Content-Disposition']='attachment; filename="1.txt"'


msg=MIMEMultipart(_to)
#邮箱正文
msg["Subject"] = "don't panic"
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
