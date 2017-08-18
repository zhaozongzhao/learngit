import swipe
def scheduleMultipoint(driver):
        driver.find_element_by_id('com.dentist.android:id/calendarBt').click()
        driver.find_element_by_id('com.dentist.android:id/addIb').click()


def time(driver):#就诊时间
        driver.find_element_by_id('com.dentist.android:id/cureHourLl').click()#就诊时间
        driver.find_element_by_name('23:00').click()#时间
        driver.find_element_by_name('00').click()#分钟
        driver.find_element_by_name('15分钟').click()#时长
        driver.find_element_by_name('完成').click()

def data(driver):#就诊日期
        driver.find_element_by_id('com.dentist.android:id/cureDayLl').click()#就诊日期
        driver.find_element_by_name('完成').click()

def patient(driver):#患者
        driver.find_element_by_id('com.dentist.android:id/patientLl').click()
        #driver.find_element_by_id('com.dentist.android:id/layout_search').send_keys('总校')
        #driver.find_element_by_id('com.dentist.android:id/contactLl').click()
        driver.find_element_by_name('总校').click()
        driver.find_element_by_name('总校').click()
def site(driver):#就诊地点
        driver.find_element_by_id('com.dentist.android:id/moreLocLl').click()#选择就诊地点
        driver.find_element_by_id('com.dentist.android:id/select_city_layout').click()
        driver.find_element_by_name('北京市').click()
        driver.find_element_by_name('返回').click()
        driver.find_element_by_name('欢乐口腔(华贸分院)').click()
def project(driver):#治疗项目
        driver.find_element_by_name('牙位/治疗项目').click()
        driver.find_element_by_name('修复').click()
        driver.find_element_by_name('备牙').click()
        driver.find_element_by_name('保存').click()
        swipe.swipeUp(driver)
        driver.find_element_by_name('发起预约').click()
        driver.find_element_by_name('继续保存').click()

def subscribe(driver):
        patient(driver)
        data(driver)
        time(driver)
        site(driver)
        project(driver)



