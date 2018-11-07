k, permutation = 0, 1
while (k < 10):
    k += 1
    if (k < 6):
        continue
    permutation *= k
    if (k == 10):
        print(permutation)
        break
