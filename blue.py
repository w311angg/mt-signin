import requests
import os
import base64

cookies=os.getenv('blue_cookie')
cookies=base64.b64decode(cookies)

re=requests.get('https://h5.ele.me/restapi/biz.svip_scene/svip/engine/xSupply?params[]=%7B%22tagCode%22:%2243002%22,%22supplyInst%22:%2243002%7C178006%22,%22extra%22:%7B%22costFoodiePea%22:1000%7D%7D&bizCode=biz_code_main&longitude=111.71564899384975&latitude=29.03628185391426',headers={'user-agent':'Rajax/1 ONEPLUS_A3010/mokee_oneplus3 Android/10 Display/mokee_oneplus3-userdebug_10_QQ3A.200805.001_eng.buildb.20210412.114049_dev-keys Eleme/9.9.5 Channel/1601275086606 ID/22db4014-60f8-33e0-bd07-fd1f935d3873; KERNEL_VERSION:3.18.124-mokee-gc0fb2a7406cf API_Level:29 Hardware:88de37c80053655480d461f4c7edd16a Mozilla/5.0 (Linux; U; Android 10; zh-CN; ONEPLUS A3010 Build/QQ3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 UWS/3.22.1.65 Mobile Safari/537.36 AliApp(ELMC/9.9.5) UCBS/2.11.1.1 TTID/offical WindVane/8.5.0,UT4Aplus/0.2.30.8-ele','cookie':cookies}).json()['data'][0]['xmessage']
print(re)
