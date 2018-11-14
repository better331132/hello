class Student:
    def __init__(self,line):
        name, gender, age, score = line.strip().split(',')
        self.name = name[0]
        self.gender = gender
        self.age = age
        self.score = int(score)
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