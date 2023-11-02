#!/bin/python3
import numpy as np


list=[]
n=int(input("size: "))
list=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        l=int(input(""))
        list[i,j]=l

print(list)
listameathr=[]
listameathr+=[int(list[0,0]+list[0,1])]
athr=list[0,0]+list[0,1]+list[(n-1),(n-2)]+list[(n-1),(n-1)]
for i in range(1,n-1):
    current=0
    for j in range(i-1,i+2):
        current+=list[i,j]
    listameathr+=[int(current)]
    athr+=current
listameathr+=[int(list[(n-1),(n-2)]+list[(n-1),(n-1)])]
print(listameathr)
print(athr)
