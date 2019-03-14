def fibs():
    a=0
    b=1
    while True:
        a,b=b,a+b
        yield a


if __name__=='__main__':
    for each in fibs():
        if each > 100:
            break
        print(each)