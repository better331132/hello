from bs4 import BeautifulSoup
import requests
import urllib.parse as parse
import os.path as path

def getFileName(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

def trans_url(url):
    url_origin =  url
    res_origin = requests.get(url_origin)
    soup_origin = BeautifulSoup(res_origin.text, 'html.parser')
    sel_origin = "#mainFrame"
    uris = soup_origin.select(sel_origin)
    uri = uris[0].get('src')
    print("uri >>>>>>>>>>>>>>>>>>>>>>>>>>", uri)
    return uri

trans_url('https://blog.naver.com/korea_diary/221433346994')

# url_origin = "https://blog.naver.com/korea_diary/221433346994"
# res_origin = requests.get(url_origin)
# soup_origin = BeautifulSoup(res_origin.text, 'html.parser')
# sel_origin = "#mainFrame"
# uris = soup_origin.select(sel_origin)
# uri = uris[0].get('src')

url = "https://blog.naver.com" + trans_url('https://blog.naver.com/korea_diary/221433346994')
print(url)



# url = "https://blog.naver.com/PostView.nhn?blogId=korea_diary&logNo=221433346994&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fwww.naver.com%2F&directAccess=false"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# sel = "#SE-9311ee77-8bde-4b1f-9e02-7ea73e016f1f > div > div > a > img"
sel = "img.se-image-resource"

imgs = soup.select(sel)
print(imgs, len(imgs))

if len(imgs) < 1:
    exit()

print("--------------------------------------")
for img in imgs:
    src = img.get('src')
    print("img>>", src)
    with open("./images/" + getFileName(src), "wb") as file:
        file.write(requests.get(src).content)