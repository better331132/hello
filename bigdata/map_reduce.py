from pprint import pprint

def map(lst):
    data=[]
    for i in lst:
        key = i[15:19]
        val = i[-18:-12]
        if int(val[-1]) in [0,1,4,5,9]:
            data.append(key + "\t" + val[-6:-1])
    strdata = "\n".join(data)
    return strdata

def rdc(data):
    dic={}
    sltdata = data.split("\n")
    data=[]
    for i in sltdata:
        datum = i.split('\t')
        data.append(tuple(datum))

    for i in data:
        dic[i[0]] = -100
    string = ''
    for i in data:
        if dic[i[0]] < int(i[1]):
            dic[i[0]] = int(i[1])
            string = string + i[0] + '\t' + i[1] + '\n'
        else:
            pass
    return string

predata = '''0067011990999991950051507004+68750+023550FM-12+038299999V0203301N00671220001CN9999999N9+00001+99999999999
0043011990999991945051512004+68750+023550FM-12+038299999V0203201N00671220001CN9999999N9+00225+99999999999
0043011990999991950051518004+68750+023550FM-12+038299999V0203201N00261220001CN9999999N9-00111+99999999999
0043012650999991949032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+01117+99999999999
0043012650999991943032418004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00384+99999999999
0043012650999991945032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00167+99999999999
0043012650999991947032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9-00150+99999999999
0043012650999991949032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00117+99999999999
0043012650999991947032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00227+99999999999
0043012650999991945032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+01116+99999999999
0043012650999991943032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9-00114+99999999999
0043012650999991943032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00191+99999999999
0043012650999991949032412004+62300+010750FM-12+048599999V0202701N00461220001CN0500001N9+00131+99999999999'''

lst = predata.split('\n')
data = map(lst)
ret = rdc(data)
print(ret)

