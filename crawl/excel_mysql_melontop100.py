import pymysql
import csv, codecs
import openpyxl
import time

def get_conn(db):
    return pymysql.connect(
                host='localhost',
                user='better',
                password='1q2w3e',
                port=3306,
                db=db,
                charset='utf8')


# rows = []
# with open('./data/meltop100.csv', 'r', encoding='utf-8') as f:
#     for num, row in enumerate(csv.reader(f)):
#         if num == 0:
#             continue
#         elif num <= 100:
#             rows.append(row[0:4])
#             # rows.append([int(row[0]),row[1],row[2],int(row[3])])
#         else:
#             break
            
# with conn_betterdb:
#     cur = conn_betterdb.cursor()
#     cur.execute("truncate table Melontop")
#     sql = "insert into Melontop(rank, songname, singer, likecnt) values(%s, %s, %s, %s)"
#     cur.executemany(sql, rows)
#     conn_betterdb.commit()

sql_delete = "delete from Melontop"
sql_insert = "insert into Melontop(rank, songname, singer, likecnt) values(%s,%s,%s,%s)"
isStart = True

def save(lst):
    try:
        conn = get_conn('betterdb')
        conn.autocommit = False
        cur = conn.cursor()

        global isStart
        if isStart:
            cur.execute(sql_delete)
            isStart = False

        cur.executemany(sql_insert, lst)
        conn.commit()
        print("Affected RowCount is", cur.rowcount, "/", len(lst))

    except Exception as err:
        print("Error!!", err)
        conn.rollback()


    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")

        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)

csvFile = codecs.open("../crawl/data/meltop100.csv", "r", "utf-8")
reader = csv.reader(csvFile, delimiter=',', quotechar='"')

lst = []
save_unit = 15
for i, row in enumerate(reader):
    if i !=0 and row[0] != "계":
        lst.append([row[0] , row[1], row[2], row[3]])
    
    if len(lst) == save_unit or row[0] == "계":
        save(lst)
        lst.clear()
        time.sleep(10)



# print("00>>", lst[0])
# print("11>>", lst[1])
# del lst[0]
# del lst[ len(lst) - 1 ]

# save(lst)