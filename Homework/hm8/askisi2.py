#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
from random import random,seed
seed(299792458)

x0=float(input("x0 = "))
y0=float(input("y0 = "))#dedomena x0 y0

N,S=0,0#arxikopoiisi twn counters
while(N<5*(10**7)):#mexri to N na ftasi to 5x10**7
    x=(1.0000000000000001-(-1))*random()-1#to x kai y exei times apo [-1,1.00001)
    y=(1.0000000000000001-(-1))*random()-1#ara [-1,1]
    if x**2+y**2<1:
        N+=1#afksano ton metriti
        S+=(x-x0)**2+(y-y0)**2#afksano tin thesi
I=S/N#dierontas to poses fores mpike me tin thesi tha vroume
#tin adrania stin thesi ekeini
print("for r0=(%.2f,%.2f) the Moment of Inertia is %f"%(x0,y0,I))
'''
gia x0=0.25
kai y0=0.25
i adrania einai peripou 0.624965, diladi peripou 0.625
'''
