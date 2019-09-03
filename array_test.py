from array import array
from random import random

floats=array('d',(random() for i in range(10**7)))
print(floats[-1])
fp=open('floats.txt','wb')
floats.tofile(fp)
fp.close()
floats2=array('d')
fp=open('floats.txt','rb')
floats2.fromfile(fp,10**7)
fp.close()
floats3=array(floats.typecode, sorted(floats))
print(floats2[-1])
print(floats3[-1])
print(floats == floats2)