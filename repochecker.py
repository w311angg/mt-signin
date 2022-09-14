import httpx
from pytools.pytools import jsondump, jsonread
from pytools.pytools import jmail
import os

token=os.getenv('token')
usernames=['w311ang','w311angg']

s=httpx.Client()
headers={'authorization':'token '+token}
olddisabledrepos=set(jsonread('disabledrepos.json',set()))
disabledrepos=set(olddisabledrepos)

for username in usernames:
  resp=s.get('https://api.github.com/users/%s/repos'%username,headers=headers)
  js=resp.json()
  for repo in js:
    name=repo['name']
    fullname='%s/%s'%(username,name)
    if not fullname in disabledrepos:
      resp=s.get('https://api.github.com/repos/%s'%fullname,headers=headers)
      code=resp.status_code
      if code==403:
        #js=resp.json()
        #msg=js['message']
        #reason=js['block']['reason']
        disabledrepos.add(fullname)

newdisabledrepos=disabledrepos-olddisabledrepos
if newdisabledrepos:
  jmail('Repo Checker','%s 等仓库被封了!'%', '.join([i.split('/')[1] for i in (list(newdisabledrepos)[:2] if len(newdisabledrepos)>2 else newdisabledrepos)]),\
"""
%s
"""%'\n'.join(['* https://github.com/%s'%repo for repo in newdisabledrepos]),\
md=True)
jsondump(list(disabledrepos),'disabledrepos.json')
print('disabledrepos:',disabledrepos)
print('olddisabledrepos:',olddisabledrepos)
print('newdisabledrepos:',newdisabledrepos)
