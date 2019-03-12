import pymysql
from pprint import pprint
import bigquery
import sys
from time import time
from google.cloud import bigquery as bq
import json
import os

def get_conn(db):
    return pymysql.connect(
            host='34.85.73.154',
            user='root',
            password='1q2w3e',
            port=3306,
            db=db,
            # cursorclass=pymysql.cursors.DictCursor,
            charset='utf8')


# # with open('./bigquery.json','r') as key_file:
# #     json_key = json.load(key_file)
# #     pprint(json_key)
# keyFile = os.getenv('jsonkeyfile')
# client = bigquery.get_client(json_key_file=keyFile, readonly=False)
# # print(bool(client))
# # exit()
# DATABASE = 'betterbigquery'
# TABLE = 'Songs'

# if not client.check_table(DATABASE, TABLE):
#     table = client.create_table(DATABASE, TABLE, [{"name": "songNo", "type": "STRING"},
#                                                   {"name": "songTitle","type": "STRING"},
#                                                   {"name": "genre","type": "STRING"},
#                                                   {"name": "album","type": "RECORD","fields": [{"name": "albumNo","type": "STRING"},
#                                                                                                {"name": "albumTitle","type": "STRING"},
#                                                                                                {"name": "agency","type": "STRING"},
#                                                                                                {"name": "releaser","type": "STRING"},
#                                                                                                {"name": "releaseDate","type": "STRING"},
#                                                                                                {"name": "albumGenre","type": "STRING"},
#                                                                                                {"name": "rating","type": "STRING"},
#                                                                                                {"name": "artistNo","type": "STRING"}]
#                                                    }
#                                                   ]
#                                 )
#     print("Success??????", table )
#     print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)
# else:
#     print("Table {} already exsits".format(TABLE))

# def gendata():
#     conn = get_conn('melondb')
#     with conn:
#         cur = conn.cursor()
#         for k in range(10):
#             sql = """select s.songNo, s.songTitle,s.genre, a.* 
#                     from Song s inner join Album a on s.albumNo = a.albumNo
#                     limit %s offset %s""" % (str(100000),str(100000*k))
#             cur.execute(sql)
#             rows = cur.fetchall()
#             if not rows:
#                 print("break!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#                 break
#             else:
#                 for row in rows:
#                     songdic ={'songNo': row['songNo'],
#                             'songTitle': row['songTitle'],
#                             'genre': row['genre'],
#                             'album': {'albumNo':row['albumNo'], 
#                                         'albumTitle':row['albumTitle'], 
#                                         'agency':row['agency'],
#                                         'releaser':row['releaser'],
#                                         'releaseDate':row['releaseDate'],
#                                         'albumGenre':row['albumGenre'],
#                                         'rating':row['rating'],
#                                         'artistNo': row['artistNo']
#                                         }
#                             }
#                     yield songdic

# def pushdata():
#     pushResult = client.push_rows(DATABASE, TABLE, gendata(), insert_id_key='songNo')
#     print("Pushed Result is ", pushResult) 
# gendata()
# pushdata()
def getdata():
    conn = get_conn('melondb')
    with conn:
            Sql = '''select s.songNo, s.songTitle,s.genre, a.* 
                        from Song s inner join Album a on s.albumNo = a.albumNo'''
            cur = conn.cursor()
            cur.execute(Sql)

            cols = [ c[0] for c in cur.description ]
            albumIdx = cols.index('albumNo')
            for row in cur.fetchall():
                d = {}
                a = {}
                for i, r in enumerate(row):
                    if i < albumIdx:
                        d[ cols[i] ] = r 
                    else:
                        a[cols[i]] = r

                d['album'] = a
                yield d

# conn = get_conn('melondb')
# with conn:
#     cur = conn.cursor()
#     for k in range(10):
#         sql = """select s.songNo, s.songTitle,s.genre, a.* 
#                 from Song s inner join Album a on s.albumNo = a.albumNo
#                 limit %s offset %s""" % (str(100000),str(100000*k))
#         cur.execute(sql)
#         rows = cur.fetchall()
#         partlst = []
#         if not rows:
#             print("break!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#             break
#         else:
#             for row in rows:
#                 # print(row)
#                 # exit()
#                 songdic ={'songNo': row[0],
#                           'songTitle': row[1],
#                           'genre': row[2],
#                           'album': {'albumNo':row[3], 
#                                     'albumTitle':row[4], 
#                                     'agency':row[5],
#                                     'releaser':row[6],
#                                     'releaseDate':row[7],
#                                     'albumGenre':row[8],
#                                     'rating':row[9],
#                                     'artistNo': row[10]
#                                     }
#                           }
#                 partlst.append(songdic)
#             pushResult = client.push_rows(DATABASE, TABLE, partlst, insert_id_key='songNo')
#             print("Pushed Result is ", pushResult) 
