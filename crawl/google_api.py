from apiclient.discovery import build
from pprint import pprint

API_KEY = "AIzaSyDmkyW4Hv1tOJ8kfxUWGQw84-le6_0ObPE"  #본인의 API키

youtube = build('youtube', 'v3', developerKey=API_KEY)

search_res = youtube.search().list(
    part='snippet',
    q='파이썬',
    type='video',
    maxResults= 50
).execute()

for item in search_res['items']:
    ss = item['snippet']['channelTitle']
    print(ss)

print(len(search_res))
