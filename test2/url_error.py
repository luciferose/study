from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
url='http://192.168.3.57'
req=Request(url)
try:
    respones=urlopen(req)
except HTTPError as e:
    print('the server couldn\'t fulfill the request.')
    print('Error code:',e.code)
except URLError as e:
    print('we failed to raech a server.')
    print('reason:',e.reason)
else:
    pass