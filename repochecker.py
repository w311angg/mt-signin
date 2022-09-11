import httpx
from pytools.pytools import jsondump, jsonread
from pytools.pytools import jmail
import os

token=os.getenv('token')
usernames=['w311ang','w311angg']

s=httpx.Client()
headers={'authorization':'token '+token}
disabledrepos=jsonread('disabledrepos.json',[])

for username in usernames:
  resp=s.get('https://api.github.com/users/%s/repos'%username,headers=headers)
  js=resp.json()
  for repo in js:
    name=repo['name']
    if not name in disabledrepos:
      resp=s.get('https://api.github.com/repos/%s/%s'%(username,name),headers=headers)
      code=resp.status_code
      if code==403:
        #js=resp.json()
        #msg=js['message']
        #reason=js['block']['reason']
        disabledrepos.append('%s/%s'%(username,name))

if disabledrepos:
  jmail('Repo Checker','%s 仓库被封了!'%', '.join([i.split('/')[1] for i in disabledrepos]),\
"""
%s
"""%'\n'.join(['* https://github.com/%s'%repo for repo in disabledrepos])\
)
jsondump(disabledrepos,'disabledrepos.json')
print('disabledrepos:',disabledrepos)
print('repos:',repos)
