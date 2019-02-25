import pymysql
from pprint import pprint
import bigquery
import sys
from time import time
from google.cloud import bigquery as bq
import json

def get_conn(db):
    return pymysql.connect(
                host='34.85.73.154',
                user='root',
                password='1q2w3e',
                port=3306,
                db=db,
                cursorclass=pymysql.cursors.DictCursor,
                charset='utf8')

conn = get_conn('melondb')

# with open('./bigquery.json','r') as key_file:
#     json_key = json.load(key_file)
#     pprint(json_key)

client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)


# print(bool(client))
# exit()
DATABASE = 'betterbigquery'
TABLE = 'Songs'

if not client.check_table(DATABASE, TABLE):
    client.create_table(DATABASE, TABLE,  [{"name": "songNo", 
                                            "type": "STRING"},
                                           {"name": "songTitle",
                                            "type": "STRING"},
                                           {"name": "genre",
                                            "type": "STRING"},
                                           {"name": "album",
                                            "type": "RECORD",
                                            "fields": [{"name": "albumNo",
                                                        "type": "STRING"},
                                                       {"name": "albumTitle",
                                                        "type": "STRING"},
                                                       {"name": "agency",
                                                        "type": "STRING"},
                                                       {"name": "releaser",
                                                        "type": "STRING"},
                                                       {"name": "releaseDate",
                                                        "type": "STRING"},
                                                       {"name": "albumGenre",
                                                        "type": "STRING"},
                                                       {"name": "rating",
                                                        "type": "STRING"},
                                                       {"name": "artistNo",
                                                        "type": "STRING"}
                                                      ]
                                            }
                                           ]
                       )
    
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)
else:
    print("Table {} already exsits".format(TABLE))

start2 = time()
with conn:
    cur = conn.cursor()
    for k in range(10):
        sql = """select s.songNo, s.songTitle,s.genre, a.* 
                from Song s inner join Album a on s.albumNo = a.albumNo
                limit %s offset %s""" % (str(100000),str(100000*k))
        cur.execute(sql)
        rows = cur.fetchall()
        partlst = []
        if not rows:
            print("break!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        else:
            for i, row in enumerate(rows):
                songdic ={'songNo': row['songNo'],
                          'songTitle': row['songTitle'],
                          'genre': row['genre'],
                          'album': {'albumNo':row['albumNo'], 
                                    'albumTitle':row['albumTitle'], 
                                    'agency':row['agency'],
                                    'releaser':row['releaser'],
                                    'releaseDate':row['releaseDate'],
                                    'albumGenre':row['albumGenre'],
                                    'rating':row['rating'],
                                    'artistNo': row['artistNo']
                                    }
                          }
                partlst.append(songdic)
            pushResult = client.push_rows(DATABASE, TABLE, partlst, insert_id_key='songNo')
            print("Pushed Result is ", pushResult) 
end2 = time()
print(end2-start2) # 0.87s
