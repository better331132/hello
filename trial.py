i,factorial = 0, 1
while (i < 10):
    i += 1
    factorial *= i
    if (i == 10):
        print(factorial)
        break

k, permutation = 0, 1
while (i < 10):
    i += 1
    if (i < 6):
        continue
    permutation *= i
    if (i == 10):
        break