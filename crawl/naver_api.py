import requests, json
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "JdPJow_YardxNqZZ_Xa1",
    "X-Naver-Client-Secret": "zWrh7TvHer"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

# print( jsonData['items'])

for item in jsonData['items']:
    print(" 게시글명 : ", item['title'] + '\n',
          "게시글주소 : ", item['link'] + '\n',
          "블로거명 : ", item['bloggername'] + '\n',
          "작성일 : ", item['postdate'] + '\n')

# for item in jsonData('items')

# print(json.dumps(jsonData, ensure_ascii=False, indent=2))

# for item in jsonData['items']:
#     item['']