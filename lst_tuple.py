lst = ['a','b','c']
lst1 = []
for i in range(3):
    lst1.append(tuple(lst[i]))

data = tuple(lst1)
print(data)