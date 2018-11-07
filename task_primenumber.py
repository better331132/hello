sum = 0
for i in range(6):
    if i == 2:
        sum += i
        continue
    for k in range(2,i):
        if (i % k == 0):
            break
        elif k == (i - 1):
            sum += i
print(sum)            #김주동님 참고