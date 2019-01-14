from bs4 import BeautifulSoup
import requests
import csv

a = []
def trans_structure(x):
    return x.text.strip().replace('\n\n','').replace('\xa0', '').replace('\n','').replace('\\','').replace('※이동통신 기기에서 작성한 글입니다.','').replace(',',' ')

for i in range(150050,150100):
    url = "https://www.korean.go.kr/front/onlineQna/onlineQnaView.do?mn_id=60&qna_seq={}&pageIndex=1".format(i)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    examples=soup.select('div.board_view')
    
    for example in examples:

        divs = example.select('div.b_view_content.b_line_dot')
        # print(ps)
        if len(divs) < 2: 
            continue
        n = 0
        for div in divs:
            if div.text == '':
                continue
            n += 1
            if n == 1:
                a.append("질문 : " +  trans_structure(div) + ",")
                print("질문------------>", trans_structure(div))
                print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            if n == 2:
                a.append("답변 : " + trans_structure(div) + ",")
                print("답변>>>>>>>>>>>>>", trans_structure(div))
            
        print("=================================================================================================")

# with open('./data/국립국어원.txt','w', encoding='utf-8') as file:
#     for line in a:
#         file.write(line)
#         file.write('\n')
# print(a)
with open('./data/국국100.csv', 'w', encoding='utf-8') as file:
    m = 0
    for line in a:
        m += 1
        file.write(line)
        if (m % 2) == 0 :
            file.write("\n")

# f = open('./data/국국3.csv', 'w', encoding='euc-kr', newline='')
# wr = csv.writer(f)
# wr.writerow(a, delimiter=',')
# f.close()
