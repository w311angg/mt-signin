import requests
import os

cookies=os.getenv('zhuan_cookie')
cookies=base64.b64decode(cookies)

re=requests.post('https://app.zhuanzhuan.com/zz/v2/zzpost/zhuanall',headers={'cookie':cookies}).json()['respData']['toast']
print(re)
