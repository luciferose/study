import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context
url='https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
response=urllib.request.urlopen(url)
html=response.read()
soup=BeautifulSoup(html,'html.parser')
for keyword in ['view','item']:
    for each in soup.find_all(href=re.compile(keyword)):
        print(each.text,'->',''.join(['https://baike.baidu.com',each['href']]))