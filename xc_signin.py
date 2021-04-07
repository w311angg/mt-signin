import requests
import os

username=os.getenv('xc_username')
password=os.getenv('xc_password')

s=requests.Session()
s.get('https://cdn.79tian.com/api/wxapi/view/AppSwitch.php?inc=ajax_login&act=BannerHome')
token=s.get('https://cdn.79tian.com/api/wxapi/view/AppSwitch.php?inc=ajax_login&act=login&username=%s&password=%s'%(username,password)).json()['token']
s.get('https://cdn.79tian.com/api/wxapi/view/index.php?TokenVerify=%s'%token)
signin=s.post('https://cdn.79tian.com/api/wxapi/view/ajax/sign.ajax.php?act=Signin').json()['msg']
print(signin)
