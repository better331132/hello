numbers = [5,2,3,1,4]
sort_numbers = sorted(numbers)
print(sort_numbers)                 #리스트 배열을 다르게 하여 출력만 함
print(numbers)

numbers.sort()                      #리스트 배열을 다르게 해서 새로운 리스트를 생성
print(numbers)
numbers.sort(reverse = True)
print(numbers)

new_numbers = sorted(numbers)
print(numbers)
print(new_numbers)

t = (1, 5, 3)
print( "qqq>> ", sorted(t))

d = {'a' : 1, 'b ': 3, 'c' : 2}
k = d.values()
print("qqq>>",sorted(k))