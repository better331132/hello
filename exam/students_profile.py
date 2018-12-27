import sqlite3
grade = ['F', 'D', 'C', 'B', 'A']

class Students:
    def __init__(self, line):
        name, gender, age, score, addr = line.strip().split(',')
        self.name = name
        self.score = int(score)
        self.addr = addr
        self.kgender = gender
        self.age = int(age)

    def __str__(self):
        return "{}**\t{}\t{}대\t{}\t{}".format(self.name[0], self.egender, self.dec, self.grade, self.tad)

    def stg(self):
        if self.score == 100:
            self.grade = 'A'
        else :
            self.grade = grade[self.score // 10 - 5]
    
    def kte(self):
        if self.kgender == '남':
            self.egender = 'M'
        else :
            self.egender = 'F'
    
    def pro(self):
        self.dec = self.age - (self.age % 10)

    def adt(self):
        d = self.addr.split(' ')
        if len(d) == 5:
            self.tad = d[2] + ' ' + d[3]
        else:
            self.tad = d[1] + ' ' + d[2]


students = []
with open("../students.csv", "r", encoding = 'utf8') as file :
    for i, line in enumerate(file):
        if i == 0:
            continue
        students.append(Students(line))

students.sort( key = lambda stu : stu.score, reverse = True)

s = map(lambda stu : stu.stg(), students)
list(s)
g = map(lambda stu : stu.kte(), students)
list(g)
a = map(lambda stu : stu.pro(), students)
list(a)
t = map(lambda stu : stu.adt(), students)
list(t)



students_lst = []

for x in students:
    students_lst.append([x.name[0] + "**", x.egender, x.dec, x.grade + "대", x.tad])


conn = sqlite3.connect("exam.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name, gender, age, grade, addr) values(?,?,?,?,?)"
    cur.executemany(sql, students_lst)

    conn.commit()