from bs4 import BeautifulSoup
import requests
import re
import time
import pymysql
import json
from pprint import pprint

def crawl_rankDate(soup):
    rankDate = soup.select_one("#conts span.yyyymmdd span").text.replace('.','')
    return rankDate
def crawl_albumTitle(tr):
    albumTitle = tr.select_one("div.ellipsis.rank03 a").text
    return albumTitle
def crawl_songTitle(tr):
    songTitle = tr.select_one("div.ellipsis.rank01 > span > a").text
    return songTitle
def crawl_artistName(tr):
    artistName = tr.select_one("div.ellipsis.rank02 > a").text
    return artistName
def crawl_rank(tr):
    rank = tr.select_one('div.wrap.t_center span.rank ').text
    return rank
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
    for i in range(len(likecnt_json)):
        if likecnt_json['contsLike'][i]['CONTSID'] == songNo:
            likeCnt = likecnt_json['contsLike'][i]['SUMMCNT']
            return likeCnt

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
    genre = song_soup.select_one("#downloadfrm div.meta > dl > dd:nth-of-type(3)").text
    return genre

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
    return det_lsas


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
    return dds

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
    return rating

def crawl_dae(artistNo):
    artist_url = "https://www.melon.com/artist/timeline.htm"
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
    dl = artist_soup.select_one("#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix")
    return dl

def get_dts(artistNo):
    artist_url = "https://www.melon.com/artist/timeline.htm"
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
    dts = artist_soup.select("#conts > div.wrap_dtl_atist > div > div.wrap_atist_info > dl.atist_info.clfix > dt")
    return dts