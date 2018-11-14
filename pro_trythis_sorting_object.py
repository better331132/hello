from functools import reduce

from Student import Student  

students = []
with open('students.csv','r',encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0 : continue
        students.append(Student(line))
students.sort(key = lambda a: a.score, reverse = True)
m = map(lambda a: a.score, students)
list(m)

total = reduce(lambda x ,y : (x if type(x) == int else x.score) + y.score, students)
avg = total / len(students)

print("이름\t성별\t나이\t학점")
print("----\t----\t----\t----")
for s in students:
    print(s)

print("Total>> ", total)
print("Average>> ", avg)