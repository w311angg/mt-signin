import requests, os

token=os.getenv('token')
userid=os.getenv('userid')

s=requests.Session()
s.headers.update({'version':'3.0.30','accesstoken':token})

for i in range(15):
  i+=1
  with s.post('https://care.seewo.com/easicare/performance/score/student/69b0c3e1ab9b45768cecee4b1c5e1659',data='uid=rlqjzuovylxglhtjtnmqign74u119731&performanceId=f3d1501daa1c43a4b5e7515ea088c4b1&isNew=false&taskVersion=2&taskId=c4a7a660-45f7-4b6c-96ac-5f3ebf50d5e5',headers={'method':'POST','requesturi':'/easicare/performance/score/student/69b0c3e1ab9b45768cecee4b1c5e1659','content-type':'application/x-www-form-urlencoded; charset=utf-8'}) as resp:
    json=resp.json()
    code=json['statusCode']
    if code==200:
      print('成功点评第%s次'%i)
    else:
      raise Exception('未知原因点评失败')

with s.post('https://care.seewo.com/easicare/account/v2/daily/rlqjzuovylxglhtjtnmqign74u119731',headers={'method':'POST','requesturi':'/easicare/account/v2/daily/rlqjzuovylxglhtjtnmqign74u119731'}) as resp:
  json=resp.json()
  code=json['statusCode']
  if code==200:
    print('签到成功')
  elif code==10101:
    print('今天已签到过')
  else:
    raise Exception('未知原因签到失败')

import flower

with s.post('https://care.seewo.com/easicare-mobile/apis.json?action=SHOP_TEACHER_INDEX_INIT',json={'actionName':'SHOP_TEACHER_INDEX_INIT','params':{'token':token}}) as resp:
  json=resp.json()
  data=json['data']['data']
  unreceivedBeans=data['unreceivedBeans']
  usableBeans=data['usableBeans']

if unreceivedBeans!=0:
  with s.post('https://care.seewo.com/easicare-mobile/apis.json?action=SHOP_INDEX_HANDLE',json={'actionName':'SHOP_INDEX_HANDLE','params':{'token':token,'exchangeBeansNum':unreceivedBeans,'userId':userid}}) as resp:
    json=resp.json()
    code=json['code']
    if code==200:
      print('成功领取%s个班优豆，现有%s个'%(unreceivedBeans,usableBeans))
    elif code==40000:
      print('经验值不足，无法领取')
    else:
      print('未知错误领取失败')
else:
  print('暂无班优豆可以领取')
