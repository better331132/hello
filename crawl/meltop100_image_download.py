import requests
from bs4 import BeautifulSoup
import urllib.request
import openpyxl
import csv

url = "https://www.melon.com/chart/index.htm"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
req = urllib.request.Request(url, headers = heads)
data = urllib.request.urlopen(req).read()
soup = BeautifulSoup(data, 'html.parser')
images = soup.select("table img")

for num, image in enumerate(images):
    lnk = image.get('src')
    with open("./images/meltop100/meltop{}.png".format(num+1), "wb") as f:
        f.write(requests.get(lnk).content)



