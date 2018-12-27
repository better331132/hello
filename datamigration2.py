import pro_mig_util as mu

conn_oracle_hr = mu.get_oracle_conn("hr","hrpw", "localhost:1521/xe")
conn_mysql_dadb = mu.get_mysql_conn("dadb")
myconn = mu.get_mysql_conn("dadb")
with conn_oracle_hr:
    # cursor를 만들어줍니다
    cur = conn_oracle_hr.cursor()

    sql = '''select region_id, region_name from Regions'''

    cur.execute(sql)

    rows = cur.fetchall()

for row in rows:
    print(row)

with myconn:
    cur = myconn.cursor()
    cur.execute("drop table if exists Region")
    sql_create = '''create table Region(region_id smallint not null primary key,
                                         region_name varchar(30))
                 '''
    cur.execute(sql_create)

    sql_insert = '''insert into Region(region_id, region_name) values(%s, %s)'''
    cur.executemany(sql_insert, rows)
    print("Affectedrowcount is", cur.rowcount)

