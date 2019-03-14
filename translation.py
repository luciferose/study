import urllib.request
import urllib.parse
import json
import time

while True:
    x=input('请写入需要翻译的内容(输入q推出): ')
    if x=='q':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    head={}
    head['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    data = {}
    data['i'] = x
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15481228468870'
    data['sign'] =  'c77a142e49c48f07be09b8d4644700d3'
    data['ts'] = '1548122846887'
    data['bv'] = '7f2901ed530536104d65f4d3f630826a'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTIME'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req=urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    target=target['translateResult'][0][0]['tgt']
    print(target)
    time.sleep(2)


