import httpx
import json
import os
from pytools.pytools import secretlog

config=json.loads(os.getenv('config'))
privacyParam=config['privacyParam']
verificationHash=config['Verification-Hash']
privacyHeaderParam=config['privacy-header-param']
UserToken=config['User-Token']
Cookie=config['Cookie']

s=httpx.Client()
s.headers.update({
  'Cookie':Cookie,
  'User-Token':UserToken,
  'User-Agent':'Mozilla/5.0 (Linux; Android 12; GM1910 Build/SKQ1.211113.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4375 MMWEBSDK/20221109 Mobile Safari/537.36 MMWEBID/6025 MicroMessenger/8.0.31.2281(0x28001F37) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxcecfde2bc765c661',
  'X-DADA-ROUTE-KEY':'ADCODE',
  'App-Name':'weapp',
  'Access-Control-Allow-Origin':'*',
  'privacy-enable':'1',
  'Source-From':'H5',
  'Custom-Lat':'0',
  'Custom-Ad-Code':'0',
  'Custom-Lng':'0',
  'Channel-ID':'0',
  'Accept':'*/*',
  'X-Requested-With':'com.tencent.mm',
  'Sec-Fetch-Site':'same-origin',
  'Sec-Fetch-Mode':'cors',
  'Sec-Fetch-Dest':'empty',
  'Referer':'https://kuai.imdada.cn/toc/corp/index_v2/',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'zh-CN,zh-TW;q=0.9,zh-HK;q=0.8,zh;q=0.7,en-US;q=0.6,en;q=0.5'
})

resp=s.get('https://kuai.imdada.cn/toc/corp/growth/points/signIn',params={'privacyParam':privacyParam},headers={
  'Verification-Hash':verificationHash,
  'privacy-header-param':privacyHeaderParam,
  'content-type':'application/x-www-form-urlencoded'
})
try:
  js=resp.json()
  content=js['content']
  signinSuccess=content['checkInRewardSummary']['isCheckInFirst']
  if signinSuccess:
    print('签到成功！')
  else:
    print('签到失败，可能是已经签到过')
except Exception as e:
  raise Exception(secretlog(resp.text)) from e
