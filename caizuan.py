import httpx
import time
import random
from pytools.pytools import secretlog
from pytools.pytools import serverchen
from pytools.pytools import jsondump,jsonread
import os
from decimal import Decimal

userid=os.environ['userid']
openid=os.environ['openid']
getUserInfoSign=os.environ['sign']
targetGold=Decimal(os.environ['targetGold'])
on=os.environ['on']

config=jsonread('caizuan.json',{'targetGold':str(targetGold),'isAcheive':False})
config['targetGold']=Decimal(config['targetGold'])

if on=='schedule':
  time.sleep(random.randint(2,9)*60)

s=httpx.Client()
s.headers.update({'user-agent':'Mozilla/5.0 (Linux; Android 12; GM1910 Build/SKQ1.211113.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220903 Mobile Safari/537.36 MMWEBID/6025 MicroMessenger/8.0.28.2240(0x28001C35) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64','referer':'https://bai-piao.com/','x-requested-with':'com.tencent.mm'})

def signin():
  name='签到'

  time.sleep(random.randint(2,9))
  resp=s.get('https://bai-piao.com/app/index.php?i=2&t=0&v=1.0&from=wxapp&c=entry&a=wxapp&do=user&m=skai_tooln_a&dopost=make_sign&userid=%s&openid=%s'%(userid,openid))
  print('%s: %s'%(name,secretlog(resp.text)))
  js=resp.json()
  if js['result']=='success':
    print('%s成功!'%name)
  else:
    msg=js['msg']
    if msg=='今天已经签到，请明天再来喔~':
      print(msg)
    else:
      raise Exception('%s失败: %s'%(name,msg))
  return js

def getUserInfo():
  time.sleep(random.randint(2,9))
  resp=s.get('https://bai-piao.com/app/index.php?i=2&t=0&v=1.0&from=wxapp&c=entry&a=wxapp&do=user&m=skai_tooln_a&dopost=get_user_data&userid=%s&openid=%s&get_offline_stone_status=1&sign=%s'%(userid,openid,getUserInfoSign))
  js=resp.json()
  print('userinfo:',secretlog(resp.text))
  return js

def makeStone(power):
  name='开始采钻'

  time.sleep(random.randint(2,9))
  resp=s.get('https://bai-piao.com/app/index.php?i=2&t=0&v=1.0&from=wxapp&c=entry&a=wxapp&do=index&m=skai_tooln_a&dopost=make_stone&userid=%s&openid=%s&make_power=%s'%(userid,openid,power))
  print('%s: %s'%(name,secretlog(resp.text)))
  js=resp.json()
  if js['result']=='success':
    print('%s成功!'%name)
  else:
    msg=js['msg']
    raise Exception('%s失败: %s'%(name,msg))
  return js

userinfo=getUserInfo()
power=int(userinfo['userdata']['power'])
isMining=userinfo['make_stone_time']>0
r=signin()
if 'power' in r:
  power=r['power']
else:
  userinfo=getUserInfo()
  power=int(userinfo['userdata']['power'])
if isMining:
  print('正在采钻中，跳过')
elif power<=0:
  print('没有能量，无法采钻')
else:
  makeStone(power)

stone=Decimal(userinfo['stone'])
gold=Decimal(userinfo['gold'])
gold+=Decimal(int(stone/1000)/100)

if targetGold != config['targetGold']:
  config['targetGold']=targetGold
  config['isAcheive']=False
if gold>=targetGold:
  if not isAcheive:
    serverchen('白瓢软贝置换后已达到%s'%gold,'https://bai-piao.com/')
  config['isAcheive']=True

config['targetGold']=str(config['targetGold'])
jsondump(config,'caizuan.json')
