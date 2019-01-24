from bs4 import BeautifulSoup
import requests
import re
import time
import pymysql
import json
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
# print(songNos)
# exit()
url = "http://vlg.berryservice.net:8099/melon/list"
# url = "https://www.melon.com/chart/day/index.htm"

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
# print(songInfo_dic)
#=============================================================db와 비교하기 위해 songNo, albumNo, artistNo 추출

rankDate = bft.crawl_rankDate(soup)
conn_melondb = get_conn('melondb')
with conn_melondb:
    cur_A = conn_melondb.cursor()
    cur_B = conn_melondb.cursor()
    cur_C = conn_melondb.cursor()
    cur_D = conn_melondb.cursor()
    cur_U = conn_melondb.cursor()
    cur_M = conn_melondb.cursor()
    for i, tr in enumerate(trs):
        songNo = int(tr.attrs['data-song-no'])
        t_albumNo = tr.select_one('.wrap a').attrs['href']
        albumNo = int(re.findall(pattern_no, t_albumNo)[0])
        ass = tr.select('.ellipsis.rank02 span.checkEllipsis a')
        if (songNo,) in songNos:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#-------------------------------------------------------------------A부분SQL-------------------------------------
            rating = bft.crawl_rating(albumNo)
            likecnt_json = bft.crawl_likeCnt(songNo, songInfo_dic)
            for i in likecnt_json['contsLike']:
                if songNo == i['CONTSID']:
                    print(songNo, i['CONTSID'])
                    likeCnt = i['SUMMCNT']
            print("좋아요 >>>>>>> ", likeCnt)
            rank = bft.crawl_rank(tr)
            sql_U = "update Album set rating = %s where albumNo = %s"
            cur_U.execute(sql_U, [rating, songNo])
            sql_L = "update SongRank set likeCnt = %s where songNo = %s and rankDate = %s"
            cur_U.execute(sql_L, [likeCnt, songNo, rankDate])
            print("LikeCnt, Rating, Rank Update Success")
            print(songNo, albumNo, artistNo)

#-------------------------------------------------------------------A부분SQL-------------------------------------
    #=========================================================================================================A타입
        elif (albumNo,) in albumNos:
            for aa in ass:
                t_artistNo = aa.attrs['href']
                artistNo = int(re.findall(pattern_no, t_artistNo)[0])
                artistName = bft.crawl_artistName(tr)
                if (artistNo,) in artistNos:
                    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
#-------------------------------------------------------------------A부분SQL-------------------------------------
                    rating = bft.crawl_rating(albumNo)
                    likecnt_json = bft.crawl_likeCnt(songNo, songInfo_dic)
                    for i in likecnt_json['contsLike']:
                        if songNo == i['CONTSID']:
                            likeCnt = i['SUMMCNT']
                    rank = bft.crawl_rank(tr)
                    lst_A = [songNo, rankDate, rank, likeCnt]
                    sql_A = "insert ignore into SongRank(songNo, rankDate, rank, likeCnt) values(%s, %s, %s, %s)"
                    cur_A.execute(sql_A, lst_A)
#-------------------------------------------------------------------A부분SQL-------------------------------------
#-------------------------------------------------------------------B부분SQL-------------------------------------
                    songTitle = bft.crawl_songTitle(tr)
                    genre = bft.crawl_genre(songNo)
                    lst_B = [songNo, songTitle, genre, albumNo]
                    sql_B = """insert ignore into Song(songNo, songTitle, genre, albumNo) 
                                            values (%s, %s, %s, %s)"""
                    cur_B.execute(sql_B, lst_B)
                    for aa in ass:
                        t_artistNo = aa.attrs['href']
                        artistNo = re.findall(pattern_no, t_artistNo)[0]
                        artistName = bft.crawl_artistName(tr)
                        lst_M = [songNo, artistNo]
                        sql_M = """insert ignore into SongArtist(songNo, artistNo)
                                                values(%s, %s)"""
                        cur_M.execute(sql_M, lst_M)
                    if songNo == 3087601:
                        print("요놈은 B를 탔어야 한다.")
                        exit()
#-------------------------------------------------------------------B부분SQL-------------------------------------
#=========================================================================================================B타입
                else:
                    print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
#-------------------------------------------------------------------A부분SQL-------------------------------------
                    rating = bft.crawl_rating(albumNo)
                    likecnt_json = bft.crawl_likeCnt(songNo, songInfo_dic)
                    for i in likecnt_json['contsLike']:
                        if songNo == i['CONTSID']:
                            likeCnt = i['SUMMCNT']
                    rank = bft.crawl_rank(tr)
                    lst_A = [songNo, rankDate, rank, likeCnt]
                    sql_A = "insert ignore into SongRank(songNo, rankDate, rank, likeCnt) values(%s, %s, %s, %s)"
                    cur_A.execute(sql_A, lst_A)
#-------------------------------------------------------------------A부분SQL-------------------------------------
#-------------------------------------------------------------------B부분SQL-------------------------------------
                    songTitle = bft.crawl_songTitle(tr)
                    genre = bft.crawl_genre(songNo)
                    lst_B = [songNo, songTitle, genre, albumNo]
                    sql_B = """insert ignore into Song(songNo, songTitle, genre, albumNo) 
                                            values (%s, %s, %s, %s)"""
                    cur_B.execute(sql_B, lst_B)
                    for aa in ass:
                        t_artistNo = aa.attrs['href']
                        artistNo = re.findall(pattern_no, t_artistNo)[0]
                        artistName = bft.crawl_artistName(tr)
                        lst_M = [songNo, artistNo]
                        sql_M = """insert ignore into SongArtist(songNo, artistNo)
                                                values(%s, %s)"""
                        cur_M.execute(sql_M, lst_M)

#-------------------------------------------------------------------B부분SQL-------------------------------------
#-------------------------------------------------------------------C부분SQL-------------------------------------
                    for aa in ass:
                        t_artistNo = aa.attrs['href']
                        artistNo = re.findall(pattern_no, t_artistNo)[0]
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
                    print("이번엔 C를 타야한다.")
                    exit()
#-------------------------------------------------------------------C부분SQL-------------------------------------
#=========================================================================================================C타입
        elif (albumNo,) not in albumNos:
            for aa in ass:
                t_artistNo = aa.attrs['href']
                artistNo = int(re.findall(pattern_no, t_artistNo)[0])
                artistName = bft.crawl_artistName(tr)
                if (artistNo,) in artistNos:
                    print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
#-------------------------------------------------------------------A부분SQL-------------------------------------
                    rating = bft.crawl_rating(albumNo)
                    likecnt_json = bft.crawl_likeCnt(songNo, songInfo_dic)
                    for i in likecnt_json['contsLike']:
                        if songNo == i['CONTSID']:
                            likeCnt = i['SUMMCNT']
                    rank = bft.crawl_rank(tr)
                    lst_A = [songNo, rankDate, rank, likeCnt]
                    sql_A = "insert ignore into SongRank(songNo, rankDate, rank, likeCnt) values(%s, %s, %s, %s)"
                    cur_A.execute(sql_A, lst_A)
#-------------------------------------------------------------------A부분SQL-------------------------------------
#-------------------------------------------------------------------B부분SQL-------------------------------------
                    songTitle = bft.crawl_songTitle(tr)
                    genre = bft.crawl_genre(songNo)
                    lst_B = [songNo, songTitle, genre, albumNo]
                    sql_B = """insert ignore into Song(songNo, songTitle, genre, albumNo) 
                                            values (%s, %s, %s, %s)"""
                    cur_B.execute(sql_B, lst_B)
                    for aa in ass:
                        t_artistNo = aa.attrs['href']
                        artistNo = re.findall(pattern_no, t_artistNo)[0]
                        artistName = bft.crawl_artistName(tr)
                        lst_M = [songNo, artistNo]
                        sql_M = """insert ignore into SongArtist(songNo, artistNo)
                                                values(%s, %s)"""
                        cur_M.execute(sql_M, lst_M)
#-------------------------------------------------------------------B부분SQL-------------------------------------
#-------------------------------------------------------------------D부분SQL-------------------------------------
                    albumTitle = bft.crawl_albumTitle(tr)
                    rating = bft.crawl_rating(albumNo)
                    dds = bft.crawl_rara(albumNo)
                    lst_D = [albumNo, albumTitle, rating, artistNo]
                    sql_D = "insert ignore into Album(albumNo, albumTitle, rating, artistNo) values(%s, %s, %s, %s)"
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
                    print("이번엔 D를 타야한다.")

#-------------------------------------------------------------------D부분SQL-------------------------------------
#=========================================================================================================D타입
                else:
                    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
#-------------------------------------------------------------------A부분SQL-------------------------------------
                    rating = bft.crawl_rating(albumNo)
                    likecnt_json = bft.crawl_likeCnt(songNo, songInfo_dic)
                    for i in likecnt_json['contsLike']:
                        if songNo == i['CONTSID']:
                            print(songNo, i['CONTSID'])
                            likeCnt = i['SUMMCNT']
                    print("좋아요 >>>>>>> ", likeCnt)
                    rank = bft.crawl_rank(tr)
                    lst_A = [songNo, rankDate, rank, likeCnt]
                    sql_A = "insert ignore into SongRank(songNo, rankDate, rank, likeCnt) values(%s, %s, %s, %s)"
                    cur_A.execute(sql_A, lst_A)
#-------------------------------------------------------------------A부분SQL-------------------------------------
#-------------------------------------------------------------------B부분SQL-------------------------------------
                    songTitle = bft.crawl_songTitle(tr)
                    print("SONGNAME >>>>>>>> ", songTitle)
                    genre = bft.crawl_genre(songNo)
                    print(songTitle)
                    lst_B = [songNo, songTitle, genre, albumNo]
                    sql_B = """insert ignore into Song(songNo, songTitle, genre, albumNo) 
                                            values (%s, %s, %s, %s)"""
                    cur_B.execute(sql_B, lst_B)
                    for aa in ass:
                        t_artistNo = aa.attrs['href']
                        artistNo = re.findall(pattern_no, t_artistNo)[0]
                        artistName = bft.crawl_artistName(tr)
                        lst_M = [songNo, artistNo]
                        sql_M = """insert ignore into SongArtist(songNo, artistNo)
                                                values(%s, %s)"""
                        cur_M.execute(sql_M, lst_M)
#-------------------------------------------------------------------B부분SQL-------------------------------------
#-------------------------------------------------------------------C부분SQL-------------------------------------
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
#-------------------------------------------------------------------C부분SQL-------------------------------------
#-------------------------------------------------------------------D부분SQL-------------------------------------
                    albumTitle = bft.crawl_albumTitle(tr)
                    rating = bft.crawl_rating(albumNo)
                    dds = bft.crawl_rara(albumNo)
                    lst_D = [albumNo, albumTitle, rating, artistNo]
                    sql_D = "insert ignore into Album(albumNo, albumTitle, rating, artistNo) values(%s, %s, %s, %s)"
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
#-------------------------------------------------------------------D부분SQL-------------------------------------
    conn_melondb.commit()
#=========================================================================================================E타입
