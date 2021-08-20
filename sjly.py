import requests
import os
import sys
import xmltodict

id=os.getenv('id')

ren=requests.get('http://tt.shouji.com.cn/appv3/xml_signed.jsp?versioncode=215&jsessionid='+id)
if ren.status_code==502:
  print('服务器炸了')
  sys.exit()
re=ren.text
ree = xmltodict.parse(re)
print(ree['sjly']['info'])
