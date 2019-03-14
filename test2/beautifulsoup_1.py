import urllib.request,urllib.parse,re,ssl
from bs4 import BeautifulSoup

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    keyword=input('请输入关键字：')
    keyword=urllib.parse.urlencode({'word':keyword})
    response=urllib.request.urlopen('https://baike.baidu.com/search/word?%s' % keyword)
    html=response.read()
    soup=BeautifulSoup(html,'html.parser')
    for keyword in ['view', 'item']:
        for each in soup.find_all(href=re.compile(keyword)):
            print(each.text, '->', ''.join(['https://baike.baidu.com', each['href']]))

if __name__=='__main__':
    main()