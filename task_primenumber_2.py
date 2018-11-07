i, sum = 2, 2
while (i <= 100):
    i += 1
    for k in range(2,i):
        if (i % k == 0):
            break
        elif (k == i-1):
            sum += i
    if (i == 100):
        print(sum)