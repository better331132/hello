class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return "{}:{}".format(self.name, self.score)

students = [Student("김일수", 10), Student("김이수",20), Student("김삼수",30)]

# print(students[0])

def print_student():
    print("-------------------------")
    for s in students:
        print(s)

students = sorted(students, key = lambda stu: stu.score, reverse = True)
def fn(stu): return stu.score
print_student()

