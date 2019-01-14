import requests, json
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/kin.json"

title = "파이썬"
params = {
    "query": title,
    "display": 10,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "JdPJow_YardxNqZZ_Xa1",
    "X-Naver-Client-Secret": "zWrh7TvHer"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

print(json.dumps(jsonData, ensure_ascii=False, indent=2))


for item in jsonData['items']:
    print(" 질문명 : ", item['title'] + '\n',
          "지식인주소 : ", item['link'] + '\n',
          "QnA : ", item['description'] + '\n')

# 질문과 답에 대한 간략한 정보만 뽑아올 수 있음. 단점이 너무 크다. 비추.