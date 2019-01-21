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
    sql = "select * from Subject"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute('truncate table Subject')
    
    sql = "insert into Subject(id, name, prof, classroom) values(%s, %s, %s, %s)"
    cur.executemany(sql, rows)
    conn_dadb.commit()
