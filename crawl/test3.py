import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\workspace\python\hello\chromedriver.exe')
# driver = webdriver.Chrome('/Users/jade/workspace/python/chromedriver')  # mac or linux

driver.get("https://www.korean.go.kr/front/onlineQna/onlineQnaList.do?mn_id=60&pageIndex=1")
time.sleep(2)

inputElement = driver.find_element_by_name("searchKeyword")
inputElement.send_keys("경음")
inputElement.submit()        # cf.  inputElement.send_keys(Keys.RETURN)

time.sleep(5)                # cf.  driver.implicitly_wait(5)
# driver.quit()