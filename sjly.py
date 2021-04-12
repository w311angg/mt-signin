import requests
import os
import xmltodict

id=os.getenv('id')

re=requests.get('http://tt.shouji.com.cn/appv3/xml_signed.jsp?versioncode=215&jsessionid='+id).text
ree = xmltodict.parse(re)
print(ree['sjly']['info'])
