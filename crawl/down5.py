import urllib.request as ur

def get_url(start_date, end_date):
    url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm={}&endTm={}".format(start_date, end_date)
    print(url)

get_url("2018-03-01","2018-06-05")


# saveFile = "./images/test5.html"
# mem = ur.urlopen(url).read()
# print(mem)
# with open(saveFile, mode="wb") as file:
#     file.write(mem)

# print("OK!")