#변수 Variables (문자열)
'hello'"world"
print('hello'"world")
print('hello',"world")                              #문자열 변수 사이의 ,는 결과에서 공백으로 나타남
message = "hello world"
print(message)
print(message[0:5])
print(message[:6])                                  #공백 또한 하나의 문자로 취급
print(message[:-4])
print(len(message))
print(len(message[0:6]))
print(len(message[:-8]))
print(len(message[3:len(message)]))
print(message.split(' '))
first, second = message.split(' ')
print(first, second)