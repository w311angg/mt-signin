import requests
import json
import os

token=os.getenv('token')
idlist=json.loads(os.getenv('idlist'))

s=requests.Session()
for gpid in idlist:
  param={'group_id':gpid,'access_key':token}
  with s.get('https://api.vc.bilibili.com/link_group/v1/group/detail',params=param) as resp:
    data=resp.json()['data']
    name=data['group_name']
    ownid=data['owner_uid']
    print('%s：'%name,end='')
  param=param|{'owner_id':ownid}
  with s.get('https://api.vc.bilibili.com/link_setting/v1/link_setting/sign_in',params=param) as resp:
    json=resp.json()
    msg=json['msg']
    print(msg)
