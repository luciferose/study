import re,ssl,urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
respones=urllib.request.urlopen('https://tieba.baidu.com/p/6042092615')
html=respones.read().decode('utf-8')
p=r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
imglist=re.findall(p,html)
for each in imglist:
    print(each)
