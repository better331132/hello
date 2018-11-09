def to_int(s):
    if type(s) == str:
        return int(s)
    else:
        return s

class 평행사변형:
    def area(self, a, b):
        return to_int(a) * to_int(b)
    

    print("1)평행사변형")

class 직사각형(평행사변형):
    print("2)직사각형")

class 정사각형(직사각형):
    print("3)정사각형")

사각형 = 평행사변형()

while (True):
    opt = input("사각형의 종류를 번호로 입력하세요 >>  ")
    if opt == '1':
        c = input("평행사변형의 밑변과 높이의 길이를 각각 입력하세요 >>  ")
        cs = c.split(' ')
        C1 , C2 = int(cs[0]) , int(cs[1])
        print(사각형.area(C1 , C2))
    
    elif opt == '2':
        b = input("직사각형의 가로와 세로의 길이를 각각 입력하세요 >>  ")
        bs = b.split(' ')
        B1 , B2 = int(bs[0]), int(bs[1])
        print(사각형.area(B1 , B2))


    elif opt == '3':
        a = input("정사각형 한 변의 길이를 입력하세요 >>  ")
        a1 = a + ' ' + a
        A = a1.split(' ')
        A1 , A2 = int(A[0]), int(A[1])
        print(사각형.area(A1, A2))

    elif opt == 'quit' or opt == 'exit':
        print("종료")
        break

    else :
        print("올바른 값을 입력해 주세요")