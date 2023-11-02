#Christodoulos Stylianides askisi 2
#!/bin/python3
import numpy as np
from random import random

def f(x):
    return -(x**np.pi)+np.pi*x

def montecarlo(ntries,Low,Up):
    value=0
    for i in range(ntries):
        rnd=Low+(Up-Low)*random()
        rvs=f(rnd)
        value+=rvs
    expect=(Up-Low)*(value/ntries)
    return expect
timesgian=[1000,100000,1000000]#oi times gia to ntries

xmin=0
xmax=1.72
ymin=0
ymax=3
a=2.365149657
for i in range(3):
    ntries=timesgian[i]
    Integral=montecarlo(ntries,xmin,xmax)
    print("The Mid point Value for {0:d} tries is: {1:.5f}".format(int(ntries),float(Integral-a)))


for i in range(3):
    tries=timesgian[i]
    itsin=0#it is in, sampling method euler.
    for j in range(tries):
        x=xmax*random()
        y=ymax*random()
        if(f(x)>=y):
            itsin+=1#epitixies
    Atr=(xmax)*(ymax)#area orthogoniou
    Area=itsin*Atr/tries#Area == degmatolipsia
    print("The Sample Method Value for {0:d} tries is: {1:.5f}".format(int(tries),float(Area-a)))

exit()
