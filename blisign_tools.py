import json

try:
  inlist=json.loads(input('现有数据：'))
except json.decoder.JSONDecodeError:
  inlist=[]

while True:
  gpid=int(input('群组ID：').replace('应援团号:',''))
  inlist.append(gpid)
  print(json.dumps(inlist))
