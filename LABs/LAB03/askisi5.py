#!/bin/python3
import numpy as np

lista=[]
myfile=open("lab03_prob5.dat")
for line in myfile:
    x=line.split('\n')
    lista+=[int(x[0])]
myfile.close()
x=len(lista)
for i in range(x):
    for j in range(0,i):
        if(lista[i]==lista[j]):
            print("the number %d already exists"%(lista[j]))
            break

for i in range(x):
    for j in range(i+1,x):
        if(lista[i]+lista[j]==75):
            print("({0:d},{1:d})".format(lista[i],lista[j]))
exit()
