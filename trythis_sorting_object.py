
class Student:
    def __init__(self, name, sex, age, score):
        part_name = name.split(' ')
        first_name = part_name[0]
        self.name = first_name
        self.sex = sex
        self.age = age
        self.score = score
        if score >= 90:
            self.grade = 'A'
        elif score >= 80:
            self.grade = 'B'
        elif score >= 70:
            self.grade = 'C'
        elif score >= 60:
            self.grade = 'D'
        else :
            self.grade = 'F'

    def __str__(self):
        return "{}**   {}   {}   {}".format(self.name, self.sex, self.age, self.grade)
        


students = [
    Student("김 일","M",17,75),
    Student("이 이","F",19,82),
    Student("박 삼","M",22,84),
    Student("최 사","F",21,81),
    Student("정 오","M",19,65),
    Student("서 육","M",23,91),
    Student("고 칠","F",25,45),
    Student("양 팔","M",24,89),
    Student("유 구","F",20,68),
    Student("백 십","M",24,71)
    ]

def print_student():
    print("-------------------------")
    for s in students:
        print(s)

def fn(stu):
    return stu.score

students.sort(key = lambda stu: stu.score, reverse = True)
print_student()
