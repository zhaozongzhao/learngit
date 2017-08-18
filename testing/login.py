import time

def login(driver):#密码登陆
   # driver.find_element_by_name('忽略').click()
    driver.find_element_by_id('com.dentist.android:id/passwordTv').click()
    driver.find_element_by_id('com.dentist.android:id/phoneEt').send_keys('13884167405')
    driver.find_element_by_id('com.dentist.android:id/pswEt').send_keys('123456')
    driver.find_element_by_id('com.dentist.android:id/loginBt').click()

def authCode(driver):#验证码登陆
    driver.implicitly_wait(10)
    time.sleep(3)
    driver.find_element_by_id('com.dentist.android:id/phoneEt').send_keys('18301565568')
   # driver.find_element_by_id('com.dentist.android:id/codeTv').click()
    time.sleep(0.5)
    driver.find_element_by_id('com.dentist.android:id/codeEt').send_keys('123456')
    driver.find_element_by_id('com.dentist.android:id/loginIb').click()

def weChat(driver):#微信登陆
    driver.find_element_by_id('com.dentist.android:id/wechatIb').click()
    driver.find_element_by_id('com.tencent.mm:id/gn').send_keys('18301565568')
    driver.find_element_by_id('com.tencent.mm:id/gn').send_keys('zzz284117')
    driver.find_element_by_id('com.tencent.mm:id/b9r').click()

def  exit(driver):#t退出
    driver.find_element_by_id('com.dentist.android:id/myBt').click()
    driver.find_element_by_id('com.dentist.android:id/layout_setting').click()
    driver.find_element_by_id('com.dentist.android:id/btn_logoff').click()
    driver.find_element_by_id('com.dentist.android:id/dialogBtTv').click()#是否退出

