def login(driver,user,password,f):
  f.write('\n登录界面\t')
  driver.find_element_by_xpath('//*[@id="userid"]').send_keys(user)
  driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys(password)
  driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button').click()
  test=driver.find_element_by_xpath('//*[@id="navbar-container"]/div[1]/a/small').text
  if test=='约克牙医后台管理系统':
    f.write('登录成功测试通过\t\n')
  else:
    f.write('登录测试失败\t\n')

