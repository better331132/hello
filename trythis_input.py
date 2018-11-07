a = input("input(usage: 이름,나이,성별)>> ")
if a == '':
    print("값을 입력해 주세요")
    exit()
                                                            # 구분하면 보기 좋음
if ',' not in a:                                            # if a.find(',') == -1  a라는 str안에 ,가 없다는 뜻!
    print("쉼표로 구분해 주세요")
    exit()

b = a.split(',')
if len(b) != 3:
    print("값을 3개 입력해 주세요")
    exit()    

outmsg = "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다"
print(outmsg.format(b[0], b[1], b[2]))