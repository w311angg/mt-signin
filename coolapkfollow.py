import httpx
from pytools.pytools import jsondump, jsonread, jmail, secretlog
from markdown import markdown
from datetime import datetime
import timeago
import os
import coolapk

token=os.getenv('token')
followUser=os.getenv('followuser').split(',')

headers={
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 12; GM1910 Build/SKQ1.211113.001) (#Build; OnePlus; GM1910; GM1910_11_H.26; 12) +CoolMarket/12.4-2207192-universal',
'X-Requested-With': 'XMLHttpRequest',
'X-Sdk-Int': '31',
'X-Sdk-Locale': 'zh-CN',
'X-App-Id': 'com.coolapk.market',
'X-App-Token': coolapk.get_app_token(),
'X-App-Version': '12.4',
'X-App-Code': '2207192',
'X-Api-Version': '12',
'X-App-Device': 'QRTBCOgkUTgsTat9WYphFI7kWbvFWaYByO1YjOCdjOxAjOxEkOFJjODlDI7ATNxMjM5MTOxcjMwAjN0AyOxEjNwgDNxITM2kDMzcTOgsTZzkTZlJ2MwUDNhJ2MyYzM',
'X-Dark-Mode': '0',
'X-App-Channel': 'coolapk',
'X-App-Mode': 'universal',
'X-App-Supported': '2207192',
'Cookie': token
}
s=httpx.Client(timeout=10.0)
s.headers.update(headers)

feedsData=jsonread('coolapkfollow.json',{})
newfeeds={}

def getUserFeeds(userid):
  resp=s.get('https://api2.coolapk.com/v6/user/feedList?uid=%s&page=1&showAnonymous=0&isIncludeTop=1&showDoing=1'%userid)
  js=resp.json()
  data=js['data']
  return data

def getFeedDetail(feedid,userid):
  resp=s.get('https://api2.coolapk.com/v6/feed/detail',params={'id':feedid,'fromApi':'/v6/user/feedList?uid=%s&page=1&showAnonymous=0&isIncludeTop=1&showDoing=1'%userid})
  js=resp.json()
  data=js['data']
  return data

def getFeedAuthorReply(feedid):
  resp=s.get('https://api2.coolapk.com/v6/feed/replyList?id=%s&listType=&page=1&discussMode=1&feedType=feed&blockStatus=0&fromFeedAuthor=1'%feedid)
  try:
    js=resp.json()
  except Exception as e:
    raise Exception(secretlog(resp.text)) from e
  data=js['data']
  return data

def databaseInit():
  for userid in followUser:
    if not userid in feedsData:
      feedsData[userid]=[]
    if not userid in newfeeds:
      newfeeds[userid]=[]

databaseInit()

for userid in followUser:
  data=getUserFeeds(userid)
  for feed in data:
    feedid=feed['id']
    username=feed['username']
    timestamp=feed['dateline']
    detail=getFeedDetail(feedid,userid)
    message=detail['message']
    pictures=detail['picArr']
    reply=getFeedAuthorReply(feedid)
    if '#薅羊毛小分队' in message and (not feedid in feedsData[userid]):
      feedsData[userid].append(feedid)
      newfeeds[userid].append({
        'username': username,
        'content': message.replace('<a class="feed-link-tag" href="/t/薅羊毛小分队?type=0">#薅羊毛小分队#</a> ','').replace('<a class="feed-link-tag" href="/t/薅羊毛小分队?type=0">#薅羊毛小分队#</a>',''),
        'pictures':pictures,
        'reply': [{'msg':i['message'].replace(' [图片]','').replace('[图片] ','').replace('[图片]',''),'pic':i['picArr'] if 'picArr' in i else []} for i in reply],
        'time': timeago.format(datetime.fromtimestamp(timestamp),datetime.now(),'zh_CN'),
        'link': 'https://www.coolapk.com/feed/'+str(feedid)
      })

md=''
for userid, data in newfeeds.items():
  if data:
    md+='## [%s](http://www.coolapk.com/u/%s)\n'%(data[0]['username'],userid)
    for i in data:
      md+='''\
%s • %s

%s

%s

%s

---

'''%(
  i['time'],
  i['link'],
  i['content'].replace('#','\#').replace('\n','<br>'),
  ' '.join(['[%s](%s)'%(num,piclink) for num,piclink in enumerate(i['pictures'],start=1) if piclink]),
  '\n\n'.join(
    ['%s %s'%(
      ia['msg'].replace('\n','<br>'),
      ' '.join(['[\[图片\]](%s)'%ib for ib in ia['pic']])
    ) for ia in i['reply']]
  )
)
if md:
  print(md)
  jmail('羊毛检查机','今日共有%s个羊毛'%sum([len(i) for i in newfeeds.values()]),markdown(md),html=True)

jsondump(feedsData,'coolapkfollow.json')
