import urllib.request

url='http://www.myip.cn'

proxy_support=urllib.request.ProxyHandler({'http':'221.226.162.26:9999'})

opener=urllib.request.build_opener(proxy_support)

opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html=response.read().decode('utf-8')

print(html)
