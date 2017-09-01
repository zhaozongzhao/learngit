import smtplib
from email.mime.text import MIMEText
from email.header import Header

def SendEmail(fromAdd, toAdd, subject, attachfile, htmlText):
  strFrom = fromAdd;
  strTo = toAdd;
  msg =MIMEText(htmlText);
  msg['Content-Type'] = 'Text/HTML';
  msg['Subject'] = Header(subject,'gb2312');
  msg['To'] = strTo;
  msg['From'] = strFrom;

  smtp = smtplib.SMTP('smtp.qq.com');
  smtp.login('2206321864@qq.com','kzdxkjuavfjbebhh');
  try:
    smtp.sendmail(strFrom,strTo,msg.as_string());
  finally:
    smtp.close;

if __name__ == "__main__":
  SendEmail("2206321864@qq.com","3031371046@qq.com","","hello","hello world");