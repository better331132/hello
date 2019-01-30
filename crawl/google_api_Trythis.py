from apiclient.discovery import build
from pprint import pprint
from pymongo import MongoClient, DESCENDING
  

API_KEY = "AIzaSyDmkyW4Hv1tOJ8kfxUWGQw84-le6_0ObPE"  #본인의 API키

youtube = build('youtube', 'v3', developerKey=API_KEY)

search_id_req = youtube.search().list(
    part='id',
    q='파이썬',
    type='video',
    maxResults=50
)

search_id_res = search_id_req.execute()
ids = []
for item in search_id_res['items']:
    ids.append(item['id']['videoId'])

search_snippet_req = youtube.videos().list(
    part='snippet,statistics',
    id= ",".join(ids)
)
search_snippet_res = search_snippet_req.execute()
items = search_snippet_res['items']
for item in items:
    item['statistics']['viewCount'] = int(item['statistics']['viewCount'])


mongo_client = MongoClient('localhost', 27017)
collection = mongo_client.betterdb.Youtubes
result = collection.insert_many(items)
print('Affected docs is {}'.format(len(result.inserted_ids)))

betterdb = mongo_client.get_database('betterdb')
books = betterdb.get_collection('Youtubes')

results = books.find().sort('statistics.viewCount',DESCENDING).limit(50)
for result in results:
    pprint(result['statistics']['viewCount'])



