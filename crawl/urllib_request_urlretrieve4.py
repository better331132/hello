from bs4 import BeautifulSoup
import requests

url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist.jsp?startTm=2018-01-01&endTm=2018-12-31&startSize=999&endSize=999&startLat=&endLat=&startLon=&endLon=&lat=&lon=&dist=&keyword=&x=38&y=6"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# earthquake_list = soup.select('table.table_develop')
earthquake_list = soup.select('th.top_line')
# print(card_list)

print(">>>>>>>>>", earthquake_list)
data = []
for i in earthquake_list:
    data = i.select('th.top_line')
    print("LLL>>", data)
    # tmpi = 0
    # for c in cards:
    #     games.append(data(c))

# with open("games.csv", "w", encoding='utf-8') as file:
#     file.write("게임명\t제조사\t가격\t평점\n")
#     for i in games:
#         file.write(str(i) + "\n")