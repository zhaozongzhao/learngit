import smtplib
from email.mime.text import MIMEText
_user = "2206321864@qq.com"
_pwd  = "kzdxkjuavfjbebhh"
_to   = "2206321864@qq.com.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s =smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print ("Success!")
except smtplib.SMTPException as e:
    print ("Falied,%s"%e )