example = """2
5
0 0
1 0
1 1
1 2
0 2
6
1.0 1.0
30.91 8
4.0 7.64
21.12 6.0
11.39 3.0
5.31 11.0"""

lst = example.split('\n')
totcn = int(lst.pop(0))
totalcase = []
lcn = 0
ll = len(lst)
while ll > 0:
    t_det = int(lst[lcn])
    t_lst = lst[lcn+1:lcn+1+t_det]
    tc_lst = []
    for l in t_lst:
        x, y = l.split(' ')
        tc_lst.append((x,y))
    totalcase.append(tc_lst)
    lcn= lcn+1+t_det
    ll = ll - (t_det + 1)
if len(totalcase) == totcn :
    print("Make Sense!")

print(totalcase)
distance_allcase = []
for spotA in totalcase:
    distance_elements = []
    for spoa in spotA:
        old_distance = 0
        for spob in spotA:
            if spoa == spob:
                continue
            new_distance = ((float(spoa[0])-float(spob[0]))**2 + (float(spoa[1])-float(spob[1]))**2)**0.5
            if new_distance > old_distance:
                min_distance = new_distance
                old_distance = new_distance
        distance_elements.append(min_distance)
    distance_allcase.append(distance_elements)
    print(distance_elements)
    # exit()
print(distance_allcase)
