import requests
import os
import base64

cookies=os.getenv('cookie')
cookies=base64.b64decode(cookies)

with requests.post('https://app.zhuanzhuan.com/zz/v2/zzpost/zhuanall',headers={'cookie':cookies}) as resp:
  json=resp.json()
  try:
    re=json['respData']['toast']
    print(re)
  except TypeError:
    raise Exception(json['errMsg']

