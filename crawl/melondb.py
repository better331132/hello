from bs4 import BeautifulSoup
import requests
import re
import time
import pymysql
import json
from pprint import pprint
# import codecs, csv

def get_conn(db):
    return pymysql.connect(
                host='34.85.73.154',
                user='root',
                password='1q2w3e',
                port=3306,
                db=db,
                charset='utf8')

conn = get_conn('melondb')

with conn:
    cur = conn.cursor()
    sqlsongNo = "select songNo from Song"
    cur.execute(sqlsongNo)
    songNos = cur.fetchall()
    
    sqlalbumNo = "select albumNo from Album"
    cur.execute(sqlalbumNo)
    albumNos = cur.fetchall()
    
    sqlartistNo = "select artistNo from Artist"
    cur.execute(sqlartistNo)
    artistNos = cur.fetchall()

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
pattern_artist = re.compile('\((.*)\)')


# rankDate = soup.select_one("#conts span.yyyymmdd span").text.replace('.','')
# print("rankDate >> ", rankDate)
# #============================================================================rankDate 추출

# albumTitle = tr.select_one("div.ellipsis.rank03 a").text
# print("albumTitle >> ", albumTitle)
# #============================================================================albumTitle 추출

# songTitle = tr.select_one("div.ellipsis.rank01 > span > a").text
# print("songTitle >> ", songTitle)
# #============================================================================songTitle 추출

# artistName = tr.select_one("div.ellipsis.rank02 > a").text
# print("artistName >> ", artistName)
# #============================================================================artistName 추출

# rank = tr.select_one('div.wrap.t_center span.rank ').text
# print("rank >> ", rank)
# #============================================================================rank 추출

songInfo_dic = {}
for i, tr in enumerate(trs):
    songNo = tr.attrs['data-song-no']
    t_albumNo = tr.select_one('.wrap a').attrs['href']
    albumNo = re.findall(pattern_no, t_albumNo)[0]
    t_artistNo = tr.select_one('.ellipsis.rank02 a').attrs['href']
    artistNo = re.findall(pattern_no, t_artistNo)[0]
    songInfo_dic[songNo] = {'songNo': songNo, 'albumNo': albumNo, 'artistNo': artistNo}
#=============================================================db와 비교하기 위해 songNo, albumNo, artistNo 추출

likecnt_url = "https://www.melon.com/commonlike/getSongLike.json"
likecnt_params = {
    "contsIds" : ",".join(songInfo_dic.keys())
}
likecnt_res = requests.get(likecnt_url, headers=heads, params=likecnt_params)
likecnt_json = json.loads(likecnt_res.text)
# pprint(likecnt_json)
#============================================================================likeCnt 추출

song_url = "https://www.melon.com/song/detail.htm"
song_params = {
    "songId": "{}".format(songNo)
}
song_res = requests.get(song_url, headers=heads, params=song_params)
song_html = song_res.text
song_soup = BeautifulSoup(song_html, 'html.parser')

genre = song_soup.select_one("#downloadfrm div.meta > dl > dd:nth-of-type(3)").text
print("genre >> ", genre)
#============================================================================genre 추출


det_lsas = song_soup.select("#conts > div.section_prdcr > ul > li")
for i in det_lsas:
    det_lsa = i.select_one('div.entry span.type').text
    if det_lsa == '작사':
        t_lyricist = i.select_one('div.entry a').attrs['href']
        lyricist = re.findall(pattern_artist, t_lyricist)[0]
        print("작사 >> ", lyricist)
    elif det_lsa == '작곡':
        t_songWriter = i.select_one('div.entry a').attrs['href']
        songWriter = re.findall(pattern_artist, t_songWriter)[0]
        print("작곡 >> ", songWriter)
    else:
        t_arranger = i.select_one('div.entry a').attrs['href']
        arranger = re.findall(pattern_artist, t_arranger)[0]
        print("편곡 >> ", arranger)        
#============================================================================lyricist, songWriter, arranger 추출


album_url = "https://www.melon.com/album/detail.htm"
album_params = {
    "albumId": "{}".format(albumNo)
}
album_res = requests.get(album_url, headers=heads, params=album_params)
album_html = album_res.text
album_soup = BeautifulSoup(album_html, 'html.parser')
dds = album_soup.select("div.wrap_info div.meta dd")
for i, dd in enumerate(dds):
    if i == 0:
        releaseDate = dd.text
        print("발매날짜",releaseDate)
    elif i == 1:
        albumGenre = dd.text
        print("앨범장르",albumGenre)
    elif i == 2:
        releaser = dd.text
        print("발매사",releaser)
    else:
        agency = dd.text
        print("기획사",agency)
#============================================================================agency, releaser, releaseDate, albumGenre 추출


album_json_url = "https://www.melon.com/album/albumGradeInfo.json"
album_json_params = {
    "albumId": "{}".format(albumNo)
}
album_json_res = requests.get(album_json_url, headers=heads, params=album_json_params)
album_json = json.loads(album_json_res.text)
rating = round(float(album_json['infoGrade']['TOTAVRGSCORE']) * 20, 2)
print(albumNo, rating)
#============================================================================rating 추출

artist_url = "https://www.melon.com/artist/timeline.htm"
artist_params = {
    "artistId": "{}".format(artistNo)
}
artist_res = requests.get(artist_url, headers=heads, params=artist_params)
artist_html = artist_res.text
artist_soup = BeautifulSoup(artist_html, 'html.parser')
dl = artist_soup.select_one("#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix")
dts = artist_soup.select("#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt")
rng = len(dts) + 1

for i in range(1, rng):
    categ = dl.select_one("dt:nth-of-type({})".format(i)).text
    if categ == '데뷔':
        debutDate = dl.select_one("dd:nth-of-type({}) span".format(i)).text.replace('.','')
        print("데뷔 >> ", debutDate)
    elif categ == '활동유형':
        artistType = dl.select_one("dd:nth-of-type({})".format(i)).text
        print("활동유형 >> ", artistType)
    elif categ == '소속사':
        emc = dl.select_one("dd:nth-of-type({})".format(i)).text
        print("소속사 >> ", emc)
#============================================================================artistType, emc, debutDate 추출
