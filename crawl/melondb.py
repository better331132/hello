from bs4 import BeautifulSoup
import requests
import re
import time
import pymysql
import json
from pprint import pprint
# import codecs, csv

# def get_conn(db):
#     return pymysql.connect(
#                 host='34.85.73.154',
#                 user='root',
#                 password='1q2w3e',
#                 port=3306,
#                 db=db,
#                 charset='utf8')

# conn = get_conn('melondb')

# with conn:
#     cur = conn.cursor()
#     sqlsongNo = "select songNo from Song"
#     cur.execute(sqlsongNo)
#     songNos = cur.fetchall()
    
#     sqlalbumNo = "select albumNo from Album"
#     cur.execute(sqlalbumNo)
#     albumNos = cur.fetchall()
    
#     sqlartistNo = "select artistNo from Artist"
#     cur.execute(sqlartistNo)
#     artistNos = cur.fetchall()

# print(songNos, albumNos, artistNos)


url = "https://www.melon.com/chart/day/index.htm"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

res = requests.get(url, headers=heads)
html = res.text

soup = BeautifulSoup(html, 'html.parser')
trs = soup.select("form#frm table tr")
trs.pop(0)

# print(len(trs))

pattern_no = re.compile('\(\'(.*)\'\)')
pattern_rating = re.compile('([0-9.]+)')


# def crawlA():
#     album_url = "https://www.melon.com/album/detail.htm?albumId={}".format(albumNo)
#     album_res = requests.get(url, headers=heads)
#     album_html = album_res.text
#     album_soup = BeautifulSoup(album_html, 'html.parser')
#     album_detail = album_soup.select_one("div.wrap_info")
rankDate = soup.select_one("#conts span.yyyymmdd span").text.replace('.','')
print(rankDate)



likecnt_dic = {}
for tr in trs:
    songNo = tr.attrs['data-song-no']
    t_albumNo = tr.select_one('.wrap a').attrs['href']
    albumNo = re.findall(pattern_no, t_albumNo)[0]
    t_artistNo = tr.select_one('.ellipsis.rank02 a').attrs['href']
    artistNo = re.findall(pattern_no, t_artistNo)[0]

    rank = tr.select_one('span.rank').text

    album_url = "https://www.melon.com/album/albumGradeInfo.json"
    album_params = {
        "albumId": "{}".format(albumNo)
    }
    album_res = requests.get(album_url, headers=heads, params=album_params)
    album_json = json.loads(album_res.text)
    rating = round(float(album_json['infoGrade']['TOTAVRGSCORE']) * 20, 2)
    print(albumNo, rating)
    exit()

    # if songNo not in songNos:
    #     crawlA()
    # elif albumNo not in albumNos and artistNo not in artistNos:
    #     crawlB()
    # elif albumNo not in albumNos and artistNo in artistNos:
    #     crawlC()
    # elif albumNo in albumNos and artistNo not in artistNos:
    #     crawlD()
    # else:
    #     crawlE()


    # print(songNo, albumNo, artistNo)

likecnt_url = "https://www.melon.com/commonlike/getSongLike.json"
likecnt_params = {
    "contsIds" : ",".join(dic.keys())
}
likecnt_res = requests.get(likecnt_url, headers=heads, params=likecnt_params)
likecnt_json = json.loads(likecnt_res.text)
likeCnt = likecnt_json['contsLike'][0]['SUMMCNT']



