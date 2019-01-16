import time
from bs4 import BeautifulSoup
import requests


queries = ['경음', '사이시옷', '맞춤법', '자음동화', '유음화']

data = []
data_fail = []
for query in queries:
    for i in range(1, 100):
        url = "https://kin.naver.com/search/list.nhn?query={}&page={}".format(query, i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        t_urls = soup.select('#s_content > div.section > ul > li > dl > dt > a')
        for n in range(10):
            t_url = t_urls[n].get('href')
            t_html = requests.get(t_url).text
            t_soup = BeautifulSoup(t_html, 'html.parser')
            question_title = t_soup.select_one("#content div.title")
            question_content = t_soup.select_one("#content div.c-heading__content")
            answer = t_soup.select_one("#answer_1 > div._endContents.c-heading-answer__content > div")
            if question_title != None :
                print("Question_title Exist : ", t_url, "\n\n")
                if question_content != None :
                    print("Question_content Exist : ")
                    if answer != None :
                        print("질문 : ", question_title.text.strip(), question_content.text.strip(), "\n")
                        print("답변 : ", answer.text.strip(), "\n\n\n\n")
                        print("질문(O), 내용(O), 답변(O)")
                        data.append("검색어 : " + query + '$' + "질문 : " + question_title.text.strip() + ' ' + question_content.text.strip() + '$' + "답변 : " + answer.text.strip() + '\n')
                        continue
                elif answer != None :
                    print("질문 : ", question_title.text.strip(), "\n")
                    print("답변 : ", answer.text.strip(), "\n\n\n\n")
                    print("질문(O), 내용(X), 답변(O)")
                    data.append("검색어 : " + query + '$' + "질문 : " + question_title.text.strip() + '$' + "답변 : " + answer.text.strip() + '\n')
                else:
                    print("이건 데이터가 아니야.....", t_url, "\n\n")
                    print("질문(O), 내용(X), 답변(X)")
                    data_fail.append('답변없음' + '$' + t_url + '$' + '\n')
            else :
                print("질문이 없어............", t_url, "\n\n")
                data_fail.append('질문없음' + '$' + t_url + '$' + '\n')
                    
                continue

            
            # print(question_title.text.strip())
            # print(question_content.text.strip())

with open('./data/지식인검색.csv', 'w', encoding='utf-8') as file:
    for line in data:
        file.write(line)

with open('./data/지식인검색실패.csv', 'w', encoding='utf-8') as file:
    for f_url in data_fail:
        file.write(f_url)

# with open('./data/지식인검색.csv', 'w', encoding='utf-8') as file:
#     m = 0
#     for line in data:
#         m += 1
#         file.write(line)
#         if (m % 2) == 0 :
#             file.write("\n")