import pro_mig_util as mu

conn_betterdb = mu.get_mysql_conn('betterdb')
conn_dadb = mu.get_mysql_conn('dadb')
table = 'Subject'
cols = "id, name, prof, classroom, classroom cr2"
rand_row_count = 0
# read from source db
with conn_betterdb:
    better_cnt = mu.get_count(conn_betterdb, table)

    cur = conn_betterdb.cursor()
    sql = "select " + cols + " from " + table + " order by rand() limit %s"
    rand_row_count = round(better_cnt / 3)
    cur.execute(sql, (rand_row_count,))
    better_list = cur.fetchall()

with conn_dadb:
    da_cnt = mu.get_count(conn_dadb, table)

    print("betterdb =", better_cnt, ", dadb =", da_cnt)
    if better_cnt != da_cnt:
        print("Not Valid Count!! betterdb =", better_cnt, ", dadb =", da_cnt)
        exit()

    else:
        print("Count is OK")
        cur = conn_dadb.cursor()

        sql = '''select id, name, prof, classroom
                   from Subject
                  where id = %s
                    and name = %s
                    and prof = %s
                    and (case when %s is null 
                              then classroom is null
                              else classroom = %s end)
                  '''
        cur.executemany(sql, better_list)
        curcnt = cur.rowcount

        if rand_row_count == curcnt:
            print("Whole data is OK", "Verified count is", rand_row_count)
            
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Fail",
              rand_row_count, curcnt)

        # sql = "select " + cols + " from " + table + " where id = %s"
        # for row in better_list:
        #     cur.execute(sql, row[0])
        #     r = cur.fetchone()

        #     if row[0] == r[0] and row[1] == r[1] and row[2] == r[2] and row[3] == r[3]:
        #         print(r, "OK")
        #     else:
        #         print(row, r, "Fail!!")
        #         break