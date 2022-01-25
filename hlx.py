import requests
from pytools.pytools import tomd5
import json
import os

users=json.loads(os.getenv('users'))

s=requests.Session()
s.headers.update({'User-Agent':'okhttp/3.8.1','Connection':'close','Accept-Encoding':'gzip'})

params={'platform':'2','gkey':'000000','app_version':'4.1.0.8','versioncode':'20141459','market_id':'floor_web','device_code':'[d]cc11cdd3-5d22-4794-b776-caab0088fd33','phone_brand_type':'UN','_key':''}

def login(username,password,sign):
  global params
  data={'account':username,
        'login_type':2,
        'password':tomd5(password),
        'sign':sign}
  with s.post('http://floor.huluxia.com/account/login/ANDROID/4.1.8',params=params,data=data,headers={'Content-Type':'application/x-www-form-urlencoded'}) as resp:
    json=resp.json()
    status=json['status']
    msg=json['msg']
    if status==1:
      key=json['_key']
      nick=json['user']['nick']
      print('%s***%s: 登录成功'%(nick[0],nick[-1]))
      params['_key']=key
    else:
      raise Exception('登录异常: '+msg)

def getAllCatId():
  _params=params.copy()
  _params['_key'],_params['is_hidden']='',1
  catId=[]
  with s.get('http://floor.huluxia.com/category/list/ANDROID/2.0',params=_params) as resp:
    json=resp.json()
    status=json['status']
    msg=json['msg']
    if status==1:
      categories=json['categories']
      for i in categories:
        id=i['categoryID']
        name=i['title']
        catId.append({'name':name,'id':id})
      return catId
    else:
      raise Exception('获取板块异常: '+msg)

def signin(catId):
  _params=params.copy()
  _params['cat_id']=catId
  with s.get('http://floor.huluxia.com/user/signin/ANDROID/4.0',params=_params) as resp:
    json=resp.json()
    status=json['status']
    msg=json['msg']
    return [status,msg]

for i in users:
  username=i[0]
  password=i[1]
  sign=i[2]
  login(username,password,sign)
  catId=getAllCatId()
  for i,count in zip(catId,range(len(catId))):
    id=i['id']
    name=i['name']
    signinn=signin(id)
    status=signinn[0]
    msg=signinn[1]
    if status==1:
      print('%s%s: 签到成功'%('; ' if count else '',name),end='')
    else:
      print('%s%s: %s'%('; ' if count else '',name,msg),end='')
