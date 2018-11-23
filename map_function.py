# def make_double(x):
#     return x * 2

# numbers = range(1,5)
# double_numbers = map(make_double,numbers)
# print(list(double_numbers))

# double_numbers = map(lambda x : x * 2, numbers)
# print(list(double_numbers))

numbers = range(0,101)
# div_hundred = map(lambda x : x // 10 ** 2, numbers)
# print(list(div_hundred))

a = filter(lambda x : x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 !=0 and x !=1, numbers)
b = [2, 3, 5, 7]
print(a)