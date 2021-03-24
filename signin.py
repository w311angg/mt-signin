import requests
import re
import os

username=os.getenv('username')
password=os.getenv('password')

s = requests.Session()
s.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A3010 Build/QQ3A.200805.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36'})
s.get('https://bbs.binmt.cc/')
with s.get('https://bbs.binmt.cc/member.php?mod=logging&action=login&mobile=2') as web:
  text=web.text
  loginhash=re.search('(?<=loginhash=)([^\"]*)',text).group()
  formhash=re.search('(?<=<input type=\"hidden\" name=\"formhash\" id=\"formhash\" value=\')([^\']*)',text).group()
s.post('https://bbs.binmt.cc/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=%s&handlekey=loginform&inajax=1'%(loginhash),data={'formhash':formhash,'fastloginfield':'username','cookietime':'31104000','username':username,'password':password,'questionid':0})
with s.get('https://bbs.binmt.cc/') as web:
  text=web.text
  formhash=re.search('(?<=formhash=)([^\&]*)',text).group()
a=s.get('https://bbs.binmt.cc/plugin.php?id=k_misign:sign&operation=qiandao&format=text&formhash=%s'%(formhash)).text
print(a)
