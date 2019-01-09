from bs4 import BeautifulSoup
import requests

def toFloat(s):
   return float(s.text.strip().replace(',', ''))

url = "https://www.korean.go.kr/front/onlineQna/onlineQnaView.do?mn_id=60&qna_seq=155851&pageIndex=1"
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

examples=soup.select('div.b_view_content.b_line_dot')
# print(examples)

for example in examples:
   ps = example.select('p')
   for p in ps:
       if p.text == '':
           continue
       print(p.text)

# "b_view_content b_line_dot"

# trs = soup.select('table > tbody > tr')

# for tr in trs:
#     tds = tr.select('div.b_view_content b_line_dot')
#     if (len(tds) < 4):
#         continue

#     tit = tds[0]
#     rate = tds[1]
#     diff = toFloat(tds[2]) - toFloat(tds[3])

#     print("{}, {}, {}".format(tit.text.strip(), rate.text, diff))