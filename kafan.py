import requests
import re
from os import getenv

s=requests.Session()

s.headers.update({'cookie':getenv('cookie')})

with s.get('https://bbs.kafan.cn/forum.php?mod=guide&view=hot&mobile=2') as web:
  text=web.text
  #print(text)
  if '>马上签到<' in text:
    signurl=re.search('(?<=<a href=").*(?=">马上签到</a>)',text).group().replace('amp;','')
  elif '<body class="bg">\r\n签到完毕' in text:
    print('已签到过了')
    exit()
  else:
    raise Exception('找不到签到入口，签到失败')

#signurl='https://bbs.kafan.cn/plugin.php?id=dsu_amupper&ppersubmit=true&formhash=32553b18&mobile=2'
with s.get(signurl) as web:
  text=web.text
  resp=re.search('(?<=<div class="jump_c">\r\n<p>).*(?=</p>)',text).group()
  print(resp)
