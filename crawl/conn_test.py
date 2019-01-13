import random
import pymysql
from random import randrange


# data = open('./data/국립국어원qna1.txt', 'r', encoding='utf-8')
# lines = data.read()
# data.close()

# lines = []
# with open('./data/국립국어원qna1.txt','r', encoding='utf-8') as data:
#     lin = data.readlines()
#     if 
#     lines.append(lin)

# print(lin)

lines = []

file=open('./data/국립국어원qna1.txt','r', encoding='utf-8')

while (1):
    line=file.readline()

    try:escape=line.index('\n')
    except:escape=len(line)
    
    if line:
        lines.append(line[0:escape])
    else:
        break
    
file.close()

print(lines)


# conn = pymysql.connect(host='localhost', user='better', password='1q2w3e', port=3306, db='betterdb', charset='utf8')

# with conn:
#     cur = conn.cursor()
#     sql = "insert into QnaExample(question, answer) values(%s, %s)"
#     cur.execute(sql, lines)
#     conn.commit()
