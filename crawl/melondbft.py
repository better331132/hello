from bs4 import BeautifulSoup
import requests
import re
import time
import pymysql
import json
from pprint import pprint

def crawl_rankDate(soup):
    rankDate = soup.select_one("#conts span.yyyymmdd span").text.replace('.','')

def crawl_albumTitle(tr):
    albumTitle = tr.select_one("div.ellipsis.rank03 a").text
def crawl_songTitle(tr):
    songTitle = tr.select_one("div.ellipsis.rank01 > span > a").text

def crawl_artistName(tr):
    artistName = tr.select_one("div.ellipsis.rank02 > a").text

def crawl_rank(tr):
    rank = tr.select_one('div.wrap.t_center span.rank ').text

def crawl_likeCnt(songNo, songInfo_dic):
    likecnt_url = "https://www.melon.com/commonlike/getSongLike.json"
    heads = {
        "Referer": "https: // www.melon.com/chart/index.htm",
        "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    likecnt_params = {
        "contsIds" : ",".join(songInfo_dic.keys())
    }
    likecnt_res = requests.get(likecnt_url, headers=heads, params=likecnt_params)
    likecnt_json = json.loads(likecnt_res.text)
    for i in len(likecnt_json):
        if likecnt_json['contsLike'][i]['CONTSID'] == songNo:
            likeCnt = likecnt_json['contsLike'][i]['SUMMCNT']

def crawl_genre(songNo):
    song_url = "https://www.melon.com/song/detail.htm"
    heads = {
        "Referer": "https: // www.melon.com/chart/index.htm",
        "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    song_params = {
        "songId": "{}".format(songNo)
    }
    song_res = requests.get(song_url, headers=heads, params=song_params)
    song_html = song_res.text
    song_soup = BeautifulSoup(song_html, 'html.parser')
    genre = song_soup.select_one("#downloadfrm div.meta > dl > dd:nth-child(6)").text

def crawl_lsa(songNo):
    song_url = "https://www.melon.com/song/detail.htm"
    heads = {
        "Referer": "https: // www.melon.com/chart/index.htm",
        "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    song_params = {
        "songId": "{}".format(songNo)
    }
    song_res = requests.get(song_url, headers=heads, params=song_params)
    song_html = song_res.text
    song_soup = BeautifulSoup(song_html, 'html.parser')
    pattern_artist = re.compile('\((.*)\)')
    det_lsas = song_soup.select("#conts > div.section_prdcr > ul > li")
    for i in det_lsas:
        det_lsa = i.select_one('div.entry span.type').text
        if det_lsa == '작사':
            t_lyricist = i.select_one('div.entry a').attrs['href']
            lyricist = re.findall(pattern_artist, t_lyricist)[0]
        elif det_lsa == '작곡':
            t_songWriter = i.select_one('div.entry a').attrs['href']
            songWriter = re.findall(pattern_artist, t_songWriter)[0]
        else:
            t_arranger = i.select_one('div.entry a').attrs['href']
            arranger = re.findall(pattern_artist, t_arranger)[0]

def crawl_rara(albumNo):
    album_url = "https://www.melon.com/album/detail.htm"
    heads = {
        "Referer": "https: // www.melon.com/chart/index.htm",
        "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
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
        elif i == 1:
            albumGenre = dd.text
        elif i == 2:
            releaser = dd.text
        else:
            agency = dd.text

def crawl_rating(albumNo):
    album_json_url = "https://www.melon.com/album/albumGradeInfo.json"
    heads = {
        "Referer": "https: // www.melon.com/chart/index.htm",
        "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    album_json_params = {
        "albumId": "{}".format(albumNo)
    }
    album_json_res = requests.get(album_json_url, headers=heads, params=album_json_params)
    album_json = json.loads(album_json_res.text)
    rating = round(float(album_json['infoGrade']['TOTAVRGSCORE']) * 20, 2)

def crawl_daae(artistNo):
    artist_url = "https://www.melon.com/artist/detail.htm"
    heads = {
        "Referer": "https: // www.melon.com/chart/index.htm",
        "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    artist_params = {
        "artistId": "{}".format(artistNo)
    }
    artist_res = requests.get(artist_url, headers=heads, params=artist_params)
    artist_html = artist_res.text
    artist_soup = BeautifulSoup(artist_html, 'html.parser')
    dl = artist_soup.select_one("#conts > div.section_atistinfo03 > dl")
    dts = artist_soup.select("#conts > div.section_atistinfo03 > dl > dt")
    rng = len(dts) + 1
    for i in range(1, rng):
        categ = dl.select_one("dt:nth-child({})".format((2 * i) - 1)).text
        if categ == '데뷔':
            debutDate = dl.select_one("dd:nth-child({})".format(2 * i)).text.replace('.','')
        elif categ == '유형':
            artistTypes = dl.select_one("dd:nth-child({})".format(2 * i)).text.split('|')
            artistType1 = artistTypes[0].strip()
            artistType2 = artistTypes[1].strip()
        elif categ == '소속사명':
            emc = dl.select_one("dd:nth-child({})".format(2 * i)).text

def crawlA(albumNo, soup, songNo, songInfo_dic, tr):
    crawl_rating(albumNo)
    crawl_rankDate(soup)
    crawl_likeCnt(songNo, songInfo_dic)
    crawl_rank(tr)


