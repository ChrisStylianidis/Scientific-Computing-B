#!/bin/python3
import numpy as np


lista=[]
myfile=open("lab03_prob1.dat")
for line in myfile:
    x=line.split('\n')
    lista+=[int(x[0])]
myfile.close()
lista.sort()
print("As a list:")
for i in range(4):
    for j in range(5):
        print("{0:4d}".format(lista[i*5+j]),end="")
    print()

print("As an array:")
lista=np.array(lista)
lista=lista.reshape((4,5))
print(lista)
exit()
