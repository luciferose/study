import random

w = 0
r = 0
while True:
    x = random.randint(1,10)
    y = random.randint(1,10)
    print(int(x),'*',int(y),'=')
    z=input('输入答案: ')
    if x*y == int(z):
        print('正确')
        r=r+1
    else:
        print('错误！！！正确答案是',x*y)
        w=w+1
    print('正确题目：', r)
    print('错误题目：', w)
    print('\n','----'*50,'\n')


