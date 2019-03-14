import urllib.request

respones=urllib.request.urlopen('http://placekitten.com/g/1920/1080')
cat_img=respones.read()
with open('cat_1920_1080.jpg','wb') as f:
    f.write(cat_img)