import os
import json
from pytools.pytools import tgsend
from pytools.pytools import secretlog

secrets=sorted(json.loads(os.environ['secrets']).items())
msg='\n'.join([f'{key}: `{value}`' if not '\n' in value else f'{key}: \n```{value}\n```' for key,value in secrets.items()])
print(secretlog(msg))
