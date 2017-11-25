from time import sleep
from selenium.webdriver import Remote

driver = Remote(command_executor='http://192.168.8.1:5555/wd/hub',desired_capabilities={'browserName':'chrome'})

driver.get("http://www.zgckxt.com")
sleep(3)

driver.quit()

print("Hello, world! My name is type your name")