import requests
import os

ppu=os.getenv('ppu')

re=requests.post('https://app.zhuanzhuan.com/zz/v2/zzpost/zhuanall',cookies={'PPU':ppu}).json()['respData']['toast']
print(re)
