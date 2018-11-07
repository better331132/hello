def plus(a,b):
    return(a + b)

def minus(a,b):
    return(a - b)

def mul(a,b):
    return(a * b)

def div(a,b):
    return(a / b)

bino = input("식을 입력해 주세요 ")
binos = bino.split(' ')
a = int(binos[0])
b = int(binos[2])
op = binos[1]

if op == '+':
    print(plus(a,b))
    exit()

if op == '-':
    print(minus(a,b))
    exit()

if op == '*':
    print(mul(a,b))
    exit()

if op == '/':
    print(div(a,b))
    exit()
