import requests, os, base64

data=os.getenv('sendingData').split()
for i,num in zip(data,range(len(data))):
  data[num]=base64.b64decode(i).decode("utf-8")

s=requests.Session()
for i,num in zip(data,range(len(data))):
  num+=1
  for _ in range(3):
    #print(i)
    with s.post('https://care.seewo.com/easicare-mobile/apis.json?action=SHOP_CLASS_BUILD_GIFT_SEND',data=i,headers={'content-type':'application/json'}) as resp:
      json=resp.json()
      code=json['data']['statusCode'] if json['data']!=[] else json['code']
      if code==200:
        beans=json['data']['data']['teacherBeans']
        print('%s账号赠送成功'%num)
      elif code==10121:
        print('已达到今日送花上限')
        break
      else:
        msg=json['message']
        raise Exception('送花失败: %s'%msg)
