import math

def test2(n):
    print(n**2)



def test():
    a=0
    while True:
        a=a+1
        yield a






if __name__ == '__main__':
    x=test()
    for y in x:
        if y > 1000:
            break
        else:
            test2(y)


