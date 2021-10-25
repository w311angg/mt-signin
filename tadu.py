import requests, base64, os

cookie=base64.b64decode(os.getenv('cookie'))
xclient='sdk=10;sdkVersion=29;screenSize=1080*2118;type=ONEPLUSA5010;imei=;imsi=;version=6.8.62.800018;versionCode=1254;rootPath=%2Fdata%2Fuser%2F0%2Fcom.tadu.read%2Ffiles%2F;rn=0534663563;tdcn=84F0CEA93625B6CEBF49B1D8FC5C3C8460EDF17F46A53478F2A04D491A0F1BF46F7912405ECC893C;android_id_new=06ea22a02f8555aa;localTime=1635153482324;shuZiId=Dumm5Uhlmpxw8Xqy6R1BsA3J014eXzpa7gT59osKU0DpDWJOjomtVZ8XEQT5QnPQHBxQe5DAjpiah3/jPdB+ElvQ;tdUUID=948289bb-bac4-48d5-afc5-8de3e1851a88;oaid=;package_name=zhuishu;k=%C2%98%C2%9C%C2%97%C2%97%C2%9E%C2%9C%C3%8A%C2%99%C3%8B%C2%9A%C2%9B%C3%8C%C3%8B%C2%98%C2%9E%C3%89%C2%97%C2%99%C2%9E%C3%88%C2%9D%C2%9C%C2%9D%C2%99%C2%9A%C2%99%C2%9A%C2%9F%C2%9C%C2%9B%C3%8B%C2%98%C2%9Ajnei;'

s=requests.Session()
s.headers.update({'COOKIE':cookie,'User-Agent':'Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 Mobile Safari/537.36/tdwx/zhuishuread','x-client':xclient})

with s.get('http://211.151.212.30/user/api/dailyAttendance770/signAndShow') as resp:
  json=resp.json()
  code=json['code']
  message=json['message']
  if code==100:
    data=json['data']
    signDaysStr=data['signDaysStr']
    todayPrestige=data['todayPrestige']
    tomorrowStr=data['tomorrowStr']
    print('%s，今天获得%s，%s，'%(signDaysStr,todayPrestige,tomorrowStr),end='')
  else:
    raise Exception(str(code)+' '+message)

with s.get('http://211.151.212.30/user/api/space/userInfo') as resp:
  json=resp.json()
  code=json['code']
  message=json['message']
  if code==100:
    data=json['data']
    remainPrestige=data['remainPrestige']
    print('你共有%s声望'%remainPrestige)
  else:
    raise Exception(str(code)+' '+message)
