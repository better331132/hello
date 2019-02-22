import timeit
import random
from pprint import pprint 
start = timeit.default_timer()
samples = [
    (2001, 23),
    (2002, 7),
    (2002, -12),
    (2001, 21),
    (2003, 20),
    (2005, 13),
    (2003, 3),
    (2005, -2),
    (2003, 22),
    (2001, -3),
]
for i in range(10000000):
    samples.append((random.randrange(1900,2018),random.randrange(-50, 60)))

stop = timeit.default_timer()
print('Time1: ', stop - start)
dic1={}
dic2={}
lst = []
start1 = timeit.default_timer()

#Your statements here


for i in samples:
    dic1[i[0]] = -100

for i in samples:
    if dic1[i[0]] < i[1]:
        dic1[i[0]] = i[1]
    else:
        pass
pprint(dic1)
stop1 = timeit.default_timer()
print('Time1: ', stop1 - start1)


start2 = timeit.default_timer()

#Your statements here

for i in samples:
    lst.append(i[0])
    if i[0] not in dic2.keys():
        dic2[i[0]] = i[1]
    elif dic2[i[0]] < i[1]:
        dic2[i[0]] = i[1]
    else:
        pass

pprint(dic2)
stop2 = timeit.default_timer()
print('Time2: ', stop2 - start2)

