from bs4 import BeautifulSoup
import requests
import time, random
import json
import pprint
import codecs, csv

def trans_structure(x):
    return x.text.strip().replace('\n','').replace('\t', '')

url = "https://www.melon.com/chart/index.htm"

headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'SCOUTER=x6r42imbf7pkvq; PCID=15474271513241870574604; PC_PCID=15474271513241870574604; POC=WP10',
        'Host': 'www.melon.com',
        'Referer': 'https://www.melon.com/chart/index.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequestecko) Chrome/71.0.3578.98 Safari/537.36'
}

html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
tops = soup.select('#frm tbody tr')

songs_no = []
for i in tops:
    songs_no.append(str(i.attrs['data-song-no']))

aurl = "https://www.melon.com/commonlike/getSongLike.json"

params = {
    'contsIds':','.join(songs_no)
}

ahtml = requests.get(aurl, headers = headers, params = params).text
jsonData = json.loads(ahtml, encoding='utf-8')

dic = {}
for song_no in songs_no:
    tempDic = {"CONTSID":song_no}
    dic[song_no] = tempDic
    
for j in jsonData['contsLike']:
    k = str(j['CONTSID'])
    dic[k]['likecnt'] = j['SUMMCNT']

# pprint.pprint(dic)
lines = []

likecnt_list = []
for i in tops:
    likecnt = int(dic[i.attrs['data-song-no']]['likecnt'])
    likecnt_list.append(likecnt)
    
minlikecnt = sorted(likecnt_list)[0]
total_likecnt = 0
total_difflikecnt = 0
for i in tops:
    rank = trans_structure(i.select_one('div.wrap.t_center span.rank'))
    title = trans_structure(i.select_one('div.ellipsis.rank01'))
    singer = trans_structure(i.select_one('span.checkEllipsis'))
    likecnt = int(dic[i.attrs['data-song-no']]['likecnt'])
    difflikecnt = likecnt - minlikecnt
    lines.append("{}${}${}${}${}\n".format(rank, title, singer, likecnt, difflikecnt))
    total_likecnt += likecnt
    total_difflikecnt += difflikecnt
    print(" 순위 : " + rank + "\n", 
            "곡명 : " + title + "\n", 
            "가수 : " + singer + "\n", 
            "공감수 : " + str(likecnt) + "\n",
            "공감수차 : " + str(difflikecnt) + "\n")
    

with open("./data/melon_top100.csv", "w", encoding='utf-8') as file:
    file.write("순위$곡명$가수$공감수$공감수차\n")
    for line in lines:
        file.write(line)
    file.write("$$$공감수총계${}\n".format(total_likecnt))
    file.write("$$$공감수차총계${}\n".format(total_difflikecnt))
