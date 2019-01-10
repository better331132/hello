import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\workspace\python\hello\chromedriver.exe')
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')  # mac or linux

driver.get("https://www.google.com")
time.sleep(2)

inputElement = driver.find_element_by_name("q")
inputElement.send_keys("세종대왕")
inputElement.send_keys((keys.CONTROL, "a"))
inputElement.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
driver.quit()