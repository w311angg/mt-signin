import httpx
import os

s=httpx.Client(verify=False)
s.headers.update({'User-Agent':'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6010 Build/QKQ1.190716.003;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36'})

def login(username,password):
  global s
  r=s.post('https://www.birdiesearch.com/user/login',data={'username':username,'password':password})
  return (r.status_code,r.text)

def signin():
  global s
  r=s.post('https://www.birdiesearch.com/api/user/reports')
  json=r.json()
  msg=json['msg']
  code=json['code']
  print(msg)
  return (code,msg)

if __name__=='__main__':
  username=os.environ['username']
  password=os.environ['password']
  login(username,password)
  signin()
