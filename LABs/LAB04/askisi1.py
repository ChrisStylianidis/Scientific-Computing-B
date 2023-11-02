#!/bin/python3
list=[[1,2,3,4],[4,5,6,7]]
L=[]
for i in range(1,-1,-1):
    for j in range(3,-1,-1):
        L+=(int(list[i,j]))
print(L)
