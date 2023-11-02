#!/bin/python3
import numpy as np

def sym(A,n):
    for i in range(n):
        for j in range(n):
            if(A[i][j]!=A[j][i]):
                return 0
    return 1
def trans(A,n):
    B=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            B[i,j]=A[j,i]
    return B

N=int(input("Give the size of 2D array: "))
K=int(input("Give K: "))

A=np.zeros((N,N))
for i in range(N):
    for j in range(N):
        A[i,j]=int(input(""))
