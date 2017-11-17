from selenium.webdriver import Remote

#定义主机与浏览器
list={'http://127.0.0.1:4444/wd/hub':'chrome',
      'http://127.0.0.1:4444/wd/hub':'chrome'}

for host,browser in list.items():#地址。浏览器
      print(host,browser)
      driver=Remote(
                   command_executor=host,
                   desired_capabilities={
                                         'platform':'ANY',#平台
                                         'browserName':browser,#浏览器
                                         'version':'',#版本
                                         'javascriptEnabled':True#javascript 是否启动


                                         }

                    )
      driver.get('http://www.baidu.com')
      driver.find_elemints_by_id('kw').send_keys(browser)
      driver.find_elemints_by_id('su').click()




