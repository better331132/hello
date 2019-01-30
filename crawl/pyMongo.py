import requests, json
from bs4 import BeautifulSoup
from pprint import pprint
import pymysql
import re
from pymongo import MongoClient, DESCENDING

def get_conn(db):
    return pymysql.connect(
                host='34.85.73.154',
                user='root',
                password='1q2w3e',
                port=3306,
                db=db,
                charset='utf8')

url = "https://openapi.naver.com/v1/search/book.json"

title = "mongodb"
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
items = jsonData['items']
for item in items:
    item['price'] = int(item['price'])


mongo_client = MongoClient('localhost', 27017)
collection = mongo_client.betterdb.Books
result = collection.insert_many(items)
print('Affected docs is {}'.format(len(result.inserted_ids)))
print(result.inserted_ids)

betterdb = mongo_client.get_database('betterdb')
books = betterdb.get_collection('Books')

results = books.find().sort('price',DESCENDING).limit(10)
for result in results:
    pprint(result)

# collection.delete_many({})
# betterdb = mongo_client.get_database('betterdb')
# collections = betterdb.collection_names()
# songs = betterdb.get_collection('Song')
# songs.insert({ "name": "EXO", "likecnt": 10} )
# songs.update({..}, {..}, upsert=True, multi=True)
# songs.remove({...})
# results = songs.find({"likecnt": 1})
# for result in results:
# 	print(result)