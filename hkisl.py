import requests
import pytools

try:
  with open('hkisl.txt') as f:
    outofstock=bool(f.read())
except FileNotFoundError:
  outofstock=1

s=requests.Session()
url='https://www.hkisl.net/cart.php?a=add&pid=218&language=chinese_cn'
content="""\
<a href=\"%s\">立即前往</a>"""%url
order=s.get(url).text
#if True:
if not '缺货中' in order:
  if outofstock==1:
    pytools.jmail('ISL_Check','免费VPS补货啦',content,html=True)
  outofstock=0
else:
  outofstock=1

with open('hkisl.txt','w') as f:
  f.write(str(outofstock))
