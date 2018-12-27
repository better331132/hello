import random
import pymysql
from random import randrange
import datetime, time

def random_date():
    random_days = randrange(int_delta)
    return d1 + datetime.timedelta(days=random_days)

d1 = datetime.datetime.strptime('1/1/1950', '%m/%d/%Y')
d2 = datetime.datetime.strptime('3/12/2018', '%m/%d/%Y')
int_delta = (d2 - d1).days

places = ["서울","부산","인천","대구","울산","대전","광주","경기도","강원도","충청도","전라도","경상도"]
fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")
num = ["0","1","2","3","4","5","6","7","8","9"]
albe = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
Students = []
i = 0
while len(Students)<1000:
    sung = random.choice(fam_names)
    ireum_lst = random.choices(first_names, k=2)
    ireum = ireum_lst[0]+ireum_lst[1]
    name = sung + ireum
    mid_num = random.choices(num, k = 4)
    end_num = random.choices(num, k = 4)
    email_addr = random.choices(albe, k = 12)
    midnum = "".join(mid_num)
    endnum = "".join(end_num)
    emailaddr = "".join(email_addr)
    birth = random_date()
    addr = random.choice(places)
    i += 1
    Students.append((name, "010-{}-{}".format(midnum, endnum),"{}@gamil.com".format(emailaddr), "{}".format(birth), "{}".format(addr)))

print(Students)



conn = pymysql.connect(host='localhost', user='better', password='1q2w3e', port=3306, db='betterdb', charset='utf8')

with conn:
    cur = conn.cursor()
    sql = "insert into Students(name, tel, email, birth, addr) values(%s, %s, %s, %s, %s)"
    cur.executemany(sql, Students)
    conn.commit()
