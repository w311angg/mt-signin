import requests
import base64
import os

url='https://care.seewo.com/'
accesstoken=os.getenv('token')
sendtext=os.getenv('sendtext')

s=requests.Session()
s.headers.update({'accesstoken':accesstoken,'version':'3.0.30'})
with s.get(url+'easicare/broadcast/api/v5/dynamics?size=10&minimumId=0&sortId=&page=1&type=17',headers={'method':'GET','requesturi':'/easicare/broadcast/api/v5/dynamics'}) as resp:
  content=resp.json()['data']['content']
  for i in content:
    title=str(base64.b64decode(i['title']),'utf-8')
    id=i['uid']
    if '安全打卡' in title:
      break
with s.get(url+'easicare/broadcast/api/v1/dynamics/punch/questions/%s/calendar'%id,headers={'method':'GET','requesturi':'/easicare/broadcast/api/v1/dynamics/punch/questions/%s/calendar'%id}) as resp:
  calendar=resp.json()['data']['calendar']
  for i in calendar:
    date=i['date']
    state=i['state']
    if state==0:
      break

data={'audios':[],
      'duration':1626017336,
      'homeworkId':id,
      'pictureUrls':[],
      'punchDate':date,
      'text':sendtext,
      'type':3,
      'videos':[]}
with s.post(url+'easicare/broadcast/api/v1/dynamics/punch/questions/%s/answers'%id,json=data,headers={'method':'POST','requesturi':'/easicare/broadcast/api/v1/dynamics/punch/questions/%s/answers'%id}) as resp:
  json=resp.json()
  code=json['statusCode']
  if code==200:
    print('签到成功')
  else:
    raise Exception(json['message'])
