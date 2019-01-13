import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

drvPath = 'C:\workspace\python\hello\chromedriver.exe'
driver = webdriver.Chrome(drvPath)
UserId = "better3311"
UserPw = ""

driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()
print("click big button!!")


id = driver.find_element_by_id('id')
id.send_keys(UserPw)
id.send_keys(Keys.CONTROL, "a")
id.send_keys(Keys.CONTROL, "x")
id.send_keys(Keys.TAB)
pw = driver.find_element_by_id('pw')
pw.send_keys(Keys.CONTROL, "v")
id = driver.find_element_by_id('id')
id.send_keys(UserId)
id.send_keys(Keys.CONTROL, "a")
id.send_keys(Keys.CONTROL, "x")
id.send_keys(Keys.CONTROL, "v")


pw.send_keys(Keys.RETURN)
time.sleep(10)                # cf.  driver.implicitly_wait(5)
driver.quit() # driver.close()
