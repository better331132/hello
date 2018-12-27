import pymysql

conn_betterdb = pymysql.connect(
    host='localhost',
    user='better',
    password='1q2w3e',
    port=3306,
    db='betterdb',
    charset='utf8'
)

conn_dadb = pymysql.connect(
    host='localhost',
    user='better',
    password='1q2w3e',
    port=3306,
    db='dadb',
    charset='utf8'
)

with conn_betterdb:
    cur = conn_betterdb.cursor()
    cur.execute('select count(*) from Subject')
    betterdb_count = cur.fetchone()[0]

with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute('select count(*) from Subject')
    dadb_count = cur.fetchone()[0]

if dadb_count == betterdb_count:
    print("OK")

else:
    print("You are looser!")

