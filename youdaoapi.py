import http.client
import hashlib
import urllib.request
import random

appKey='096509d050336d17'
secretKey='TEoM67YL0o42T6d3SDfx577WdF4YDVAm'
httpClient=None
myurl='/api'
q=input('please enter english: ')
fromLang='EN'
toLang='zh-CHS'
salt=random.randint(1,65535)

sign=appKey+q+str(salt)+secretKey
sign=sign.encode('utf-8')
m1=hashlib.md5()
m1.update(sign)
sign=m1.hexdigest()
myurl=myurl+'?appKey='+appKey+'&q='+urllib.request.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

try:
    httpClient=http.client.HTTPConnection('openapi.youdao.com')
    httpClient.request('GET',myurl)

    response=httpClient.getresponse()
    print(response.read().decode('utf-8'))
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()