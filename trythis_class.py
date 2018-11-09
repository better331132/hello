class 사각형:
    def __init__(self):
        print("변이 네개")

class 평행사변형(사각형):
    def __init__(self, name):
        self.name = name
        print("밑변이 a, 높이가 b인 평행사변형의 넓이는?")

    def area(self, a, b):
        return(a * b)

class 직사각형(평행사변형):
    def __init__(self, name):
        self.name = name
        print("가로가 c, 세로가 d인 직사각형의 넓이는?")

    def area(self, c, d):
        return(c * d)

class 정사각형(직사각형):
    def __init__(self, name):
        self.name = name
        print("한 변의 길이가 e인 정사각형의 넓이는?")
    
    def area(self, e):
        return(e ** 2)

사각형A = 평행사변형("a=3, b=4")
print(사각형A.name)
print(사각형A.area(3, 4))


사각형B = 직사각형("c=4, d=5")
print(사각형B.name)
print(사각형B.area(4, 5))

사각형C = 정사각형("e=7")
print(사각형C.name)
print(사각형C.area(7))