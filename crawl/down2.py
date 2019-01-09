import urllib.request as ur

url = "http://www.weather.go.kr/repositary/image/cht/img/g213_asia_post_grph_ft12_surfce_pa4_2019010800.s000.gif"

saveFile = "./images/test3.png"
mem = ur.urlopen(url).read()
print(mem)
with open(saveFile, mode="wb") as file:
    file.write(mem)

print("OK!")