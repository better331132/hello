class 평행사변형:
    def area(self, C1, C2):
        return(C1 * C2)

class 직사각형(평행사변형):
    def area(self, B1, B2):
        return(B1 * B2)

class 정사각형(직사각형):
    def area(self, A):
        return(A ** 2)

사각형A = 정사각형()
사각형B = 직사각형()
사각형C = 평행사변형()

while (True):
    opt = input("사각형의 종류를 번호로 입력하세요. 1)정사각형 2) 직사각형 3)평행사변형 >>  ")
    if opt == '1':
        a1 = input("정사각형 한 변의 길이를 입력하세요 >>  ")
        A = int(a1)
        print(사각형A.area(A))
    
    elif opt == '2':
        b1 = input("직사각형의 가로와 세로의 길이를 각각 입력하세요 >>  ")
        b1s = b1.split(' ')
        B1 , B2 = int(b1s[0]), int(b1s[1])
        print(사각형B.area(B1 , B2))

    elif opt == '3':
        c1 = input("평행사변형의 밑변과 높이의 길이를 각각 입력하세요 >>  ")
        c1s = c1.split(' ')
        C1 , C2 = int(c1s[0]) , int(c1s[1])
        print(사각형C.area(C1 , C2))