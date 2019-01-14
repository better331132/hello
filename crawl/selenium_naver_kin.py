import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

# drvPath = 'C:\workspace\chromedriver.exe'
# driver = webdriver.Chrome(drvPath)


# driver.get("https://kin.naver.com/search/list.nhn")
# time.sleep(1)


# query = '경음'

# search = driver.find_element_by_id('nx_query')
# search.send_keys(query)
# search.send_keys(Keys.RETURN)
                # cf.  driver.implicitly_wait(5)


# time.sleep(10)                # cf.  driver.implicitly_wait(5)
# driver.quit() # driver.close()
query = '경음'

url = "https://kin.naver.com/search/list.nhn?query={}&page=1".format(query)
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

soup.html.

# t_url = soup.select('#s_content > div.section > ul > li > dl > dt > a')
# print(t_url, len(t_url))