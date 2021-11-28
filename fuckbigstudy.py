import requests
import os

s=requests.Session()
#s.verify=False
with open('fuckbigstudy.conf') as f:
  lines=f.read().splitlines()
  cookie=lines[0]
  wxtk=lines[2]
s.headers.update({'Cookie':cookie,'User-Agent':'Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3135 MMWEBSDK/20210902 Mobile Safari/537.36 MMWEBID/6025 MicroMessenger/8.0.15.2001(0x28000F41) Process/tools WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64'})

def fuckstudy():
  ids=[]
  for i in range(1,100):
    with s.post('http://dxx.hngqt.org.cn/project/list',data={'page':i,'pageSize':10}) as resp:
      json=resp.json()
      studylist=json['data']['list']
      if not studylist:
        break
      ids+=studylist
  
  for i in ids:
    id=i['project_id']
    name=i['name']
    successes=[]
    with s.post('http://dxx.hngqt.org.cn/historystudy/studyHistoryAdd',data={'projectId':id}) as resp:
      json=resp.json()
      success=json['success']
      if success:
        successes.append(True)
      else:
        successes.append(False)
    with s.post('http://dxx.hngqt.org.cn/study/studyAdd',data={'projectId':id}) as resp:
      json=resp.json()
      success=json['success']
      if success:
        successes.append(True)
      else:
        successes.append(False)
    if successes==[True,True]:
      print('%s：学习成功！'%name)
    else:
      raise Exception("%s：学习失败"%name)

def fuckread():
  #s.verify=False
  articles=[]
  for i in range(1,100):
    with s.get('https://wx.58deep.com/projecthn/projecthnPageList?wxopenid=%s&limit=10&page=%s'%(wxtk,i)) as resp:
      json=resp.json()
      data=json['data']
      articles+=data
      if not data:
        break
  for i in articles:
    id=i['id']
    title=i['title']
    with s.get('https://wx.58deep.com/projecthn/studyHnProjectAdd?projectId=%s&wxopenid=%s'%(id,wxtk)) as resp:
      json=resp.json()
      success=json['success']
      if success:
        print('《%s》阅读成功'%title)
      else:
        raise Exception("《%s》阅读失败"%title)

fuckstudy()
fuckread()
