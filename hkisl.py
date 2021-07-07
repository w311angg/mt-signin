import requests

s=requests.Session()
order=s.get('https://www.hkisl.net/cart.php?a=add&pid=218&language=chinese_cn').text
if not '缺货中' in order:
  
