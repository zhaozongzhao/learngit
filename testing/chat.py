
def text(driver,message):
    driver.find_element_by_id('com.dentist.android:id/msgEt').click()
    driver.find_element_by_id('com.dentist.android:id/msgEt').send_keys(message)
    driver.find_element_by_id('com.dentist.android:id/faceIb').click()
    driver.find_element_by_name('发送').click()


def main(driver):

   # for i in range(100):
   driver.find_element_by_id('com.dentist.android:id/maskView').click()
   for i in range(73,100):
     text(driver,i)



if __name__ == '__main__':
    main()