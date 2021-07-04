import requests
import os

username=os.getenv('username')
password=os.getenv('password')

s=requests.Session()
s.headers.update({'user-agent':'Mozilla/5.0 (Linux; Android 9; ONEPLUS A3010 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36'})
s.get('https://cdn.79tian.com/api/wxapi/view/AppSwitch.php?inc=ajax_login&act=BannerHome')
token=s.get('https://cdn.79tian.com/api/wxapi/view/AppSwitch.php?inc=ajax_login&act=login&username=%s&password=%s'%(username,password)).json()['token']
s.get('https://cdn.79tian.com/api/wxapi/view/index.php?TokenVerify=%s'%token)
s.get('https://cdn.79tian.com/api/wxapi/view/home/sign.php')
signin=s.post('https://cdn.79tian.com/api/wxapi/view/ajax/sign.ajax.php?act=Signin').json()['msg']
print(signin)
