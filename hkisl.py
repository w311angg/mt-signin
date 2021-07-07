import requests
import pytools

with open('hkisl.txt') as f:
  try:
    outofstock=bool(f.read())
  except FileNotFound:
    outofstock=0

s=requests.Session()
url='https://www.hkisl.net/cart.php?a=add&pid=218&language=chinese_cn'
content="""\
<a href=\"%s\">立即前往</a>"""%url
order=s.get(url).text
#if True:
if (not '缺货中' in order) and outofstock==0:
  outofstock=0
  pytools.jmail('ISL_Check','免费VPS补货啦',content,html=True)
else:
  outofstock=1

with open('hkisl.txt','w') as f:
  f.write(str(outofstock))
