import collections

def ysf(a,b):
    d = collections.deque(range(1,a+1))
    c = []
    while d:
        d.rotate(-b)
        c.append(d.pop())
    print(c[-2:])

if __name__ == '__main__':
    ysf(41,3)