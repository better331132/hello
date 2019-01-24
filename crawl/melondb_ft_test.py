from bs4 import BeautifulSoup
import requests
import re
import time
import pymysql
import json
from pprint import pprint
import melondbft as bft
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
print(songNos, albumNos, artistNos)
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

pattern_no = re.compile('\(\'(.*)\'\)')
pattern_artist = re.compile('\((.*)\)')

songInfo_dic = {}
for i, tr in enumerate(trs):
    songNo = tr.attrs['data-song-no']
    t_albumNo = tr.select_one('.wrap a').attrs['href']
    albumNo = re.findall(pattern_no, t_albumNo)[0]
    ass = tr.select('.ellipsis.rank02 a')
    for aa in ass:
        t_artistNo = aa.attrs['href']
        artistNo = re.findall(pattern_no, t_artistNo)[0]
        songInfo_dic[songNo] = {'songNo': songNo, 'albumNo': albumNo, 'artistNo': artistNo}

#=============================================================db와 비교하기 위해 songNo, albumNo, artistNo 추출
rankDate = bft.crawl_rankDate(soup)

conn_melondb = get_conn('melondb')
with conn_melondb:
    cur_A = conn_melondb.cursor()
    cur_B = conn_melondb.cursor()
    cur_C = conn_melondb.cursor()
    cur_D = conn_melondb.cursor()
    cur_U = conn_melondb.cursor()
    for i, tr in enumerate(trs):
        songNo = tr.attrs['data-song-no']
        t_albumNo = tr.select_one('.wrap a').attrs['href']
        albumNo = re.findall(pattern_no, t_albumNo)[0]
        ass = tr.select('.ellipsis.rank02 span.checkEllipsis a')
        for aa in ass:
            t_artistNo = aa.attrs['href']
            artistNo = re.findall(pattern_no, t_artistNo)[0]
            if songNo in songNos:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                
                
                rating = bft.crawl_rating(albumNo)
                likeCnt = bft.crawl_likeCnt(songNo, songInfo_dic)
                rank = bft.crawl_rank(tr)
                lst_A = [songNo, rankDate, rank]
                sql_A = "insert into SongRank(songNo, rankDate, rank) values(%s, %s, %s)"
                cur_A.execute(sql_A, lst_A)
                sql_U = "update Album set rating = %s where songNo = %s"
                cur_U.execute(sql_U, [rating, songNo])
                sql_L = "update SongRank set likeCnt = %s where songNo = %s and rankDate = %s"
                cur_U.execute(sql_L, [likeCnt, songNo, rankDate])

        #=========================================================================================================A타입
            elif albumNo in albumNos and artistNo in artistNos:
                print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                
                
                rating = bft.crawl_rating(albumNo)
                likeCnt = bft.crawl_likeCnt(songNo, songInfo_dic)
                rank = bft.crawl_rank(tr)
                lst_A = [songNo, rankDate, rank]
                sql_A = "insert into SongRank(songNo, rankDate, rank) values(%s, %s, %s)"
                cur_A.execute(sql_A, lst_A)
                sql_U = "update Album set rating = %s where songNo = %s"
                cur_U.execute(sql_U, [rating, songNo])
                sql_L = "update SongRank set likeCnt = %s where songNo = %s and rankDate = %s"
                cur_U.execute(sql_L, [likeCnt, songNo, rankDate])

                songTitle = bft.crawl_songTitle(tr)
                genre = bft.crawl_genre(songNo)
                
                
                det_lsas = bft.crawl_lsa(songNo)
                
                
                lyricists = []
                songWriters = []
                arrangers = []
                for i in det_lsas:
                    det_lsa = i.select_one('div.entry span.type').text
                    if det_lsa == '작사':
                        t_lyricist = i.select_one('div.entry a').attrs['href']
                        lyricist = re.findall(pattern_artist, t_lyricist)[0]
                        lyricists.append(lyricist)
                    elif det_lsa == '작곡':
                        t_songWriter = i.select_one('div.entry a').attrs['href']
                        songWriter = re.findall(pattern_artist, t_songWriter)[0]
                        songWriters.append(songWriter)
                    else:
                        t_arranger = i.select_one('div.entry a').attrs['href']
                        arranger = re.findall(pattern_artist, t_arranger)[0]
                        arrangers.append(arranger)
                    for lyricist in lyricists:
                        for songWriter in songWriters:
                            for arranger in arrangers:
                                lst_B = [songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo]
                                sql_B = """insert into Song(songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo ) 
                                                     values(%s, %s, %s, %s, %s, %s, %s, %s)"""
                                cur_B.execute(sql_B)
                    
        #=========================================================================================================B타입
            elif albumNo in albumNos and artistNo not in artistNos:
                print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
                
                
                rating = bft.crawl_rating(albumNo)
                likeCnt = bft.crawl_likeCnt(songNo, songInfo_dic)
                rank = bft.crawl_rank(tr)
                lst_A = [songNo, rankDate, rank]
                sql_A = "insert into SongRank(songNo, rankDate, rank) values(%s, %s, %s)"
                cur_A.execute(sql_A, lst_A)
                sql_U = "update Album set rating = %s where songNo = %s"
                cur_U.execute(sql_U, [rating, songNo])
                sql_L = "update SongRank set likeCnt = %s where songNo = %s and rankDate = %s"
                cur_U.execute(sql_L, [likeCnt, songNo, rankDate])

                songTitle = bft.crawl_songTitle(tr)
                genre = bft.crawl_genre(songNo)
                
                
                det_lsas = bft.crawl_lsa(songNo)
                
                
                lyricists = []
                songWriters = []
                arrangers = []
                for i in det_lsas:
                    det_lsa = i.select_one('div.entry span.type').text
                    if det_lsa == '작사':
                        t_lyricist = i.select_one('div.entry a').attrs['href']
                        lyricist = re.findall(pattern_artist, t_lyricist)[0]
                        lyricists.append(lyricist)
                    elif det_lsa == '작곡':
                        t_songWriter = i.select_one('div.entry a').attrs['href']
                        songWriter = re.findall(pattern_artist, t_songWriter)[0]
                        songWriters.append(songWriter)
                    else:
                        t_arranger = i.select_one('div.entry a').attrs['href']
                        arranger = re.findall(pattern_artist, t_arranger)[0]
                        arrangers.append(arranger)
                    for lyricist in lyricists:
                        for songWriter in songWriters:
                            for arranger in arrangers:
                                lst_B = [songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo]
                                sql_B = """insert into Song(songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo ) 
                                                     values(%s, %s, %s, %s, %s, %s, %s, %s)"""
                                cur_B.execute(sql_B)

                artistName = bft.crawl_artistName(tr)
                dl = bft.crawl_dae(artistNo)
                
                
                dts = bft.get_dts(artistNo)
                
                
                rng = len(dts) + 1
                lst_C = [artistNo, artistName]
                sql_C = "insert ignore into Artist(artistNo, artistName) values(%s, %s)"
                cur_C.execute(sql_C, lst_C)
                
                for i in range(1, rng):
                    categ = dl.select_one("dt:nth-of-type({})".format(i)).text
                    if categ == '데뷔':
                        debutDate = dl.select_one("dd:nth-of-type({}) span".format(i)).text.replace('.','')
                        sql_U = "update Artist set debutDate = %s where artistNo = %s"
                        cur_C.execute(sql_U, [debutDate, artistNo])
                    elif categ == '활동유형':
                        artistType = dl.select_one("dd:nth-of-type({})".format(i)).text
                        sql_U = "update Artist set artistType = %s where artistNo = %s"
                        cur_C.execute(sql_U, [artistType, artistNo])
                    elif categ == '소속사':
                        emc = dl.select_one("dd:nth-of-type({})".format(i)).text
                        sql_U = "update Artist set emc = %s where artistNo = %s"
                        cur_C.execute(sql_U, [emc, artistNo])
                    else:
                        continue
        #=========================================================================================================C타입
            elif albumNo not in albumNos and artistNo in artistNos:
                print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                
                
                rating = bft.crawl_rating(albumNo)
                likeCnt = bft.crawl_likeCnt(songNo, songInfo_dic)
                rank = bft.crawl_rank(tr)
                lst_A = [songNo, rankDate, rank]
                sql_A = "insert into SongRank(songNo, rankDate, rank) values(%s, %s, %s)"
                cur_A.execute(sql_A, lst_A)
                sql_U = "update Album set rating = %s where songNo = %s"
                cur_U.execute(sql_U, [rating, songNo])
                sql_L = "update SongRank set likeCnt = %s where songNo = %s and rankDate = %s"
                cur_U.execute(sql_L, [likeCnt, songNo, rankDate])

                songTitle = bft.crawl_songTitle(tr)
                genre = bft.crawl_genre(songNo)
                
                
                det_lsas = bft.crawl_lsa(songNo)
                
                
                lyricists = []
                songWriters = []
                arrangers = []
                for i in det_lsas:
                    det_lsa = i.select_one('div.entry span.type').text
                    if det_lsa == '작사':
                        t_lyricist = i.select_one('div.entry a').attrs['href']
                        lyricist = re.findall(pattern_artist, t_lyricist)[0]
                        lyricists.append(lyricist)
                    elif det_lsa == '작곡':
                        t_songWriter = i.select_one('div.entry a').attrs['href']
                        songWriter = re.findall(pattern_artist, t_songWriter)[0]
                        songWriters.append(songWriter)
                    else:
                        t_arranger = i.select_one('div.entry a').attrs['href']
                        arranger = re.findall(pattern_artist, t_arranger)[0]
                        arrangers.append(arranger)
                    for lyricist in lyricists:
                        for songWriter in songWriters:
                            for arranger in arrangers:
                                lst_B = [songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo]
                                sql_B = """insert into Song(songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo ) 
                                                     values(%s, %s, %s, %s, %s, %s, %s, %s)"""
                                cur_B.execute(sql_B)

                albumTitle = bft.crawl_albumTitle(tr)
                dds = bft.crawl_rara(albumNo)
                
                
                rating = bft.crawl_rating(albumNo)
                
                
                lst_D = [albumNo, albumTitle, rating]
                sql_D = "insert ignore into Album(albumNo, albumTitle, rating) values(%s, %s, %s)"
                cur_D.execute(sql_D, lst_D)
                for i, dd in enumerate(dds):
                    if i == 0:
                        releaseDate = dd.text.replace('.','')
                        sql_U = "update Album set releaseDate = %s where albumNo = %s"
                        cur_D.execute(sql_U, [releaseDate, albumNo])
                    elif i == 1:
                        albumGenre = dd.text
                        sql_U = "update Album set albumGenre = %s where albumNo = %s"
                        cur_D.execute(sql_U, [albumGenre, albumNo])
                    elif i == 2:
                        releaser = dd.text
                        sql_U = "update Album set releaser = %s where albumNo = %s"
                        cur_D.execute(sql_U, [releaser, albumNo])
                    else:
                        agency = dd.text
                        sql_U = "update Album set agency = %s where albumNo = %s"
                        cur_D.execute(sql_U, [agency, albumNo])
                
        #=========================================================================================================D타입
            else:
                print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                
                rating = bft.crawl_rating(albumNo)
                likeCnt = bft.crawl_likeCnt(songNo, songInfo_dic)
                rank = bft.crawl_rank(tr)

                songTitle = bft.crawl_songTitle(tr)
                print("SONGNAME >>>>>>>> ", songTitle)
                genre = bft.crawl_genre(songNo)
                
                
                det_lsas = bft.crawl_lsa(songNo)
                
                
                lyricists = []
                songWriters = []
                arrangers = []
                for i in det_lsas:
                    det_lsa = i.select_one('div.entry span.type').text
                    if det_lsa == '작사':
                        t_lyricist = i.select_one('div.entry a').attrs['href']
                        lyricist = re.findall(pattern_artist, t_lyricist)[0]
                        lyricists.append(lyricist)
                    elif det_lsa == '작곡':
                        t_songWriter = i.select_one('div.entry a').attrs['href']
                        songWriter = re.findall(pattern_artist, t_songWriter)[0]
                        songWriters.append(songWriter)
                    else:
                        t_arranger = i.select_one('div.entry a').attrs['href']
                        arranger = re.findall(pattern_artist, t_arranger)[0]
                        arrangers.append(arranger)
                    for lyricist in lyricists:
                        for songWriter in songWriters:
                            for arranger in arrangers:
                                lst_B = [songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo]
                                sql_B = """insert into Song(songNo, songTitle, artistNo, genre, lyricist, songWriter, arranger, albumNo) 
                                                     values (%s, %s, %s, %s, %s, %s, %s, %s)"""
                                cur_B.execute(sql_B, lst_B)

                albumTitle = bft.crawl_albumTitle(tr)
                rating = bft.crawl_rating(albumNo)
                
                
                dds = bft.crawl_rara(albumNo)
                
                
                lst_D = [albumNo, albumTitle, rating]
                sql_D = "insert ignore into Album(albumNo, albumTitle, rating) values(%s, %s, %s)"
                cur_D.execute(sql_D, lst_D)
                for i, dd in enumerate(dds):
                    if i == 0:
                        releaseDate = dd.text.replace('.','')
                        print(releaseDate)
                        sql_U = "update Album set releaseDate = %s where albumNo = %s"
                        cur_D.execute(sql_U, [releaseDate, albumNo])
                    elif i == 1:
                        albumGenre = dd.text
                        sql_U = "update Album set albumGenre = %s where albumNo = %s"
                        cur_D.execute(sql_U, [albumGenre, albumNo])
                    elif i == 2:
                        releaser = dd.text
                        sql_U = "update Album set releaser = %s where albumNo = %s"
                        cur_D.execute(sql_U, [releaser, albumNo])
                    else:
                        agency = dd.text
                        sql_U = "update Album set agency = %s where albumNo = %s"
                        cur_D.execute(sql_U, [agency, albumNo])

                artistName = bft.crawl_artistName(tr)
                dl = bft.crawl_dae(artistNo)
                
                
                dts = bft.get_dts(artistNo)
                
                
                rng = len(dts) + 1
                lst_C = [artistNo, artistName]
                sql_C = "insert ignore into Artist(artistNo, artistName) values(%s, %s)"
                cur_C.execute(sql_C, lst_C)
                
                for i in range(1, rng):
                    categ = dl.select_one("dt:nth-of-type({})".format(i)).text
                    if categ == '데뷔':
                        debutDate = dl.select_one("dd:nth-of-type({}) span".format(i)).text.replace('.','')
                        sql_U = "update Artist set debutDate = %s where artistNo = %s"
                        cur_C.execute(sql_U, [debutDate, artistNo])
                    elif categ == '활동유형':
                        artistType = dl.select_one("dd:nth-of-type({})".format(i)).text
                        sql_U = "update Artist set artistType = %s where artistNo = %s"
                        cur_C.execute(sql_U, [artistType, artistNo])
                    elif categ == '소속사':
                        emc = dl.select_one("dd:nth-of-type({})".format(i)).text
                        sql_U = "update Artist set emc = %s where artistNo = %s"
                        cur_C.execute(sql_U, [emc, artistNo])
                    else:
                        continue
conn_melondb.commit()
#=========================================================================================================E타입
