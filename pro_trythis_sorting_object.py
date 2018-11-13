

class Student:
    def __init__(self,line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = age
        self.score = int(score)

    def trans_score(self):
        if self.score >= 90:
            self.grade = 'A'
        elif self.score >= 80:
            self.grade = 'B'
        elif self.score >=70:
            self.grade = 'C'
        elif self.score >= 60:
            self.grade = 'D'
        else :
            self.grade = 'F'
            
    def __str__(self):
        return "{}**\t{}\t{}\t{}".format(self.name, self.gender, self.age, self.grade)            

students = []
with open('students.csv','r',encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0 : continue
        students.append(Student(line))
students.sort(key = lambda a: a.score, reverse = True)
m = map(lambda a: a.score, students)
list(m)

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)