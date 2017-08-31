#发送邮箱的地址
import  smtplib
from email.mime.text import  MIMEText
from email.header import Header

#发送邮箱服务起的地址
smtpserver='smtp.qq.com'

#发送邮箱的用户名密码
user='2206321864@qq.com'
password='kzdxkjuavfjbebhh'

#发送邮件

sender='2206321864@qq.com'

#接收邮箱

receiver='3031371046@qq.com'

#发送邮箱主题

subject = '测试邮件地址'

#邮箱正文

msg=MIMEText('你好')
msg['To'] = strTo;
msg['From'] = strFrom;
msg['subject']=Header(subject,'utf-8')

#L连接发送短信

smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmain(sender,receiver,msg.as_string())
smtp.quit()
