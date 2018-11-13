int_numbers = range(0, 100)
print(list(int_numbers))

even_numbers = filter(lambda x : x % 2 == 0, int_numbers)
print(list(even_numbers))

def fn(x):
    if x % 2 == 0:
        return x

even_numbers = filter(fn, int_numbers)
print(list(even_numbers))                                       #메모리 주소에 값을 넣는게 =, 값의 비교는 ==

