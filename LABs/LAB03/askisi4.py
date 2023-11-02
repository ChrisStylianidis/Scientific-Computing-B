#!/bin/python3
import numpy as np
lista=[]
myfile=open("lab03_prob4.dat")
for line in myfile:
    x=line.split('\n')
    lista+=[int(x[0])]
myfile.close()
sum=0
gin=1
mesos=0
for i in lista:
    sum+=i*i#gia a
    gin*=(1-i)#gia b
    mesos+=i#gia c
print("(a)",sum) 
print("(b)",gin)
mesos/=len(lista)
print("(c)",mesos)
athr=0
for a in lista:
    athr+=((a-mesos)**2)
athr/=len(lista)
print("(d)",np.sqrt(athr))
exit()
