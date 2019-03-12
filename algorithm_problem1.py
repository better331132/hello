# import timeit
# start = timeit.default_timer()

# sample = [example1, example2, example3, example4]
def aaa(x):
    lst = x.strip().split('\n')
    elements = []
    for ls in lst:
        element = ls.split(' ')
        elements.append(element)
    cn = len(elements[1])
    rn = len(elements)-1
    coordinates = {}
    for i in range(cn):
        for k in range(rn):
            if elements[k+1][i] == '0':
                continue
            coordinates[elements[k+1][i]] = [int(k+1),int(i+1)]
    ops = []
    ck = coordinates.values()
    for j in coordinates.keys():
        for l in coordinates.keys():
            if int(j)<int(l):
                rdiff = abs(coordinates[j][0] - coordinates[l][0])
                cdiff = abs(coordinates[j][1] - coordinates[l][1])
                if cdiff == 1:
                    ops.append([int(j),int(l)])
                elif rdiff == 1:
                    ops.append([int(j),int(l)])
                else:
                    det = min(rdiff,cdiff)
                    if det == 0 and coordinates[j] != coordinates[l]:
                        det = max(rdiff,cdiff)
                        pass
                    t_det = 0
                    for a in range(1,det):
                        nbp = [(coordinates[j][0]*(det - a) + coordinates[l][0]*a) /det,(coordinates[j][1]*(det - a) + coordinates[l][1]*a) /det]
                        if nbp in ck:
                            t_det += 1 
                            continue
                    if t_det == 0:
                        ops.append([int(j),int(l)])

    s = int(elements[0][-1])
    last = int(elements[-1][-1])
    i = 1
    cs = []
    while s <= last:
        if [i,s] in ops:
            cs.append(i)
        i += 1
        s += 1
    print(len(cs))
    for y in cs:
        print(y)
example1 = """
3 4 6
1 2 3 0
0 5 4 0
0 6 7 8"""
aaa(example1)
example2 = """
3 4 7
1 2 3 0
0 5 4 0
0 6 7 8"""
aaa(example2)
example3 = """
3 4 5
1 8 9 10
2 7 6 11
3 4 5 12"""
aaa(example3)
example4 = """
5 3 5
1 2 3
0 0 4
7 6 5
8 0 0
9 10 11"""
aaa(example4)

# end = timeit.default_timer()
# print(end-start)