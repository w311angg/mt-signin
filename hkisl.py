import requests
import pytools

s=requests.Session()
url='https://www.hkisl.net/cart.php?a=add&pid=218&language=chinese_cn'
content="""\
<a href=\"%s\">立即前往</a>"""%url
order=s.get(url).text
if not '缺货中' in order:
  pytools.jmail('ISL_Check','免费VPS补货啦',content,html=True)
