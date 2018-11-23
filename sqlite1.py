# import sqlite3
 
# conn = sqlite3.connect("test.db")
 
# with conn:
#     cur = conn.cursor()
#     sql = "select * from Student where id=? or name=?"
#     cur.execute(sql, (2, '림리'))
#     rows = cur.fetchall()
 
#     for row in rows:
#         print(row)

# import sqlite3

# conn = sqlite3.connect("test.db")

# data = (
#     (21, '홍길동'),
#     (22, '홍길순')
# )

# with conn:
#     cur = conn.cursor()
#     sql = "insert into tt(id, name) values(?,?)"
#     cur.executemany(sql, data)

#     conn.commit()

import random
import sqlite3

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

data = []
i = 0
while len(data)<100:
    sung = random.choice(fam_names)
    ireum_lst = random.choices(first_names, k=2)
    ireum = ireum_lst[0]+ireum_lst[1]
    name = sung + ireum
    i += 1
    data.append((name, ))

data = tuple(data)
print(data)


conn = sqlite3.connect("test.db")


with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"
    cur.executemany(sql, data)

    conn.commit()