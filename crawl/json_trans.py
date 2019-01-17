from bs4 import BeautifulSoup
from pprint import pprint
html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
        <th>D사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
        <td>광주</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
        <td>100명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
        <td>062-121-1212</td>

    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
        <td>d@d.com</td>
    </tr>
</table>
'''
def daum(th):
    return th.next.next.next

soup = BeautifulSoup(html,'html.parser')


trs = soup.select('table tr')
ths = soup.select('table tr th')
cates = []
for i, tr in enumerate(trs):
    if i == 0:
        for j, th in enumerate(tr.select('th')):
            if j == 0: continue
            cates.append(th.text)
print(cates)
companies = {}

for i in range(len(cates)):
    for num, tr in enumerate(trs):
        tr_list = tr.text.strip().split('\n')
        tr_list.pop(0)
        elm =tr_list[i]
        if num == 0:
            cpname = elm
        elif num == 1:
            addr = elm
        elif num == 2:
            employees = elm
        elif num == 3:
            tel = elm
        else:
            email = elm
    companies[cpname] = {'주소': addr, '직원수': employees, '전화번호': tel, '대표메일': email}

pprint(companies)
# while True:
#     company_name = input("회사의 이름을 입력해주세요. ({})".format(','.join(cates)))
#     element = input("원하는 정보를 입력해주세요. (대표메일, 전화번호, 주소)")
#     print(companies[company_name][element])
#     det = input("계속 할거?")
#     if det == 'n' or det == 'ㅜ':
#         print("종료")
#         break
#     else:
#         print("계속")
