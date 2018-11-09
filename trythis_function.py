def plus(a,b):
    return(a + b)

def minus(a,b):
    return(a - b)

def mul(a,b):
    return(a * b)

def div(a,b):            
    return(a / b)

while (True) :
    bino = input("식을 입력해 주세요 ")
    binos = bino.split(' ')
    a = int(binos[0])
    b = int(binos[2])
    op = binos[1]

    if op == '+':
        r = plus(a,b)

    elif op == '-':
        r = minus(a,b)

    elif op == '*':
        r = mul(a,b)

    else :
        r = div(a,b)

    if op == '/':
        print("Answer is {:.2f}".format(r))

    else :
        print("Answer is {:d}".format(r))

    if r >= 100000000 :
        break