i, sum = 0, 0
while (i >= 0):
    i += 1
    if (i % 2 == 0):
        continue
    sum += i
    if (i == 99):
        print(sum)
        break