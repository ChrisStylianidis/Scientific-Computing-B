#!/bin/python3
import numpy as np

lista=[]
myfile=open("inp_integers.dat")
for line in myfile:
    x=line.split('\n')
    lista+=[int(x[0])]
myfile.close()
ar=np.zeros(31)
for i in lista:
    ar[i]+=1
for i in range(1,31):
    if(ar[i]==1):
        print("The number {0:2d} was found {1:6d} time".format(i,int(ar[i])))
    else:
        print("The number {0:2d} was found {1:6d} times".format(i,int(ar[i])))
exit()
