import itchat, time
from itchat.content import *
import os

realname=os.getenv('wx_name')
@itchat.msg_register(TEXT, isGroupChat=True)
#@itchat.msg_register(TEXT)
def text_reply(msg):
    text=msg.text
    if ('平安接龙' in text) and (not '%s平安'%realname in text):
        lastline=text.split('\n')[-1]
        #print(lastline)
        number=int(lastline.split('.')[0])
        mynum=number+1
        mytext=text+'\n%s. %s平安'%(realname,mynum)
        msg.user.send(mytext)
        os._exit(0)

itchat.auto_login(hotReload=True)
itchat.run(True)