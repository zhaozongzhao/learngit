def sendTelMsg(msg, phoneID):
  SendTelMsgUrl="http://www.810086.com.cn/jk.aspx"
  params = {"zh":"china", "mm":"china@10086",
       "hm":phoneID,"nr":msg,"sms_type":88}
  postData=urllib.urlencode(params)
  req = urllib2.Request(SendTelMsgUrl, postData)
  req.add_header('Content-Type', "application/x-www-form-urlencoded")
  respone = urllib2.urlopen(req)
  res = respone.read()
  return res