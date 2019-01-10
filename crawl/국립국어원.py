from bs4 import BeautifulSoup
import requests

a = []
def trans_structure(x):
    return x.text.strip().replace('\n\n','').replace('\xa0', '').replace('\n','').replace('\\','')

for i in range(156000,156100):
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
                a.append("질문 : " + trans_structure(div))
                print("질문------------>", trans_structure(div))
                print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            if n == 2:
                a.append("답변 : " + trans_structure(div) + "\n")
                print("답변>>>>>>>>>>>>>", trans_structure(div))
            
        print("=================================================================================================")

with open('./data/국립국어원.txt','w', encoding='utf-8') as file:
    for line in a:
        file.write(line)
        file.write('\n')
