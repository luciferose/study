import urllib.request
import os
import hash

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a=html.find('current-comment-page') + 23
    b=html.find(']',a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs=[]
    a = html.find('<span class="img-hash">')
    while a != -1:
        b=html.find('</span>',a,a+255)
        if b != -1:
            img_addrs.append(html[a+23:b])
        else:
            b = a + 23
        a = html.find('<span class="img-hash">',b)
        return img_addrs



def save_imgs(folder,img_addrs):
    content = 'CJnxgemql-ACFctiYAod3sUFyQ'
    for each in img_addrs:
        each1=hash.parse(each,content)
        filename=each1.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open('http:'+each1)
            f.write(img)


def download(folder='testdownload',pages=30):
    os.mkdir(folder)
    os.chdir(folder)

    url='http://jandan.net/ooxx/'
    page_num =int(get_page(url))

    for i in range(pages):
        page_num -=1
        page_url= url + 'page-' + str(page_num) + '#comments'
        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__=='__main__':
    download()