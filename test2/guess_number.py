from random import *

answer=randint(1,100)


while True:
    putnum = int(input('in put the number: '))
    if putnum > answer:
        print('big!!!!!')
        continue
    if putnum < answer:
        print('small!!!')
        continue
    if putnum == answer:
        print('bigo right !!!!')
        break
