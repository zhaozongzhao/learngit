from time import sleep
from selenium.webdriver import Remote

driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities={'browserName':'chrome'})

driver.get("http://www.zgckxt.com")
sleep(3)

driver.quit()