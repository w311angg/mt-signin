import httpx
from pytools.pytools import jsondump, jsonread
from pytools.pytools import jmail
import os

token=os.getenv('token')
usernames=['w311ang','w311angg']

s=httpx.Client()
headers={'authorization':'token '+token}
nowrepos=set()
oldrepos=set(jsonread('repos.json',set()))

for username in usernames:
  resp=s.get('https://api.github.com/users/%s/repos'%username,headers=headers)
  js=resp.json()
  for repo in js:
    name=repo['name']
    nowrepos.add('%s/%s'%(username,name))
jsondump(list(nowrepos),'repos.json')

nowrepos-={'w311ang/AutoApiSecret-1'}
deletedrepos=oldrepos-nowrepos
disabledrepos=[]
for repo in deletedrepos:
  splited=repo.split('/')
  username=splited[0]
  reponame=splited[1]
  resp=s.get('https://api.github.com/repos/%s/%s'%(username,reponame),headers=headers)
  code=resp.status_code
  if code==403:
    js=resp.json()
    msg=js['message']
    reason=js['block']['reason']
    disabledrepos.append(repo)

if disabledrepos:
  jmail('Repo Checker','%s 仓库被封了!'%', '.join(disabledrepos),\
"""
%s
"""%'\n'.join(['* https://github.com/%s'%repo for repo in disabledrepos])\
)
print('disabledrepos:',disabledrepos)
print('deletedrepos:',deletedrepos)
print('nowrepos:',nowrepos)
print('oldrepos:',oldrepos)
