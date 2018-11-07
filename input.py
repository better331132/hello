a = input("input(usage: 이름, 나이, 성별)>> ")

outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다."
b = a.split(',')
print(outmsg.format(b[0],b[1],b[2]))
