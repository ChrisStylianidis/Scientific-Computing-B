#Christodoulos Stylianides Askisi 6
#!/bin/python3
import numpy as np

def fix(word):
    ans=""
    for i in word:
        if (i>='A' and i<='Z'):
            ans+=i.lower()
        if (i>='a' and i<='z'):
            ans+=i
    return ans

def sort(A,B):
    sort=False
    while(sort==False):
        sort=True
        for i in range(len(A)-1):
            if(A[i]<A[i+1]):
                k=A[i+1]
                A[i+1]=A[i]
                A[i]=k
                k=B[i+1]
                B[i+1]=B[i]
                B[i]=k
                sort=False
    return A,B

myfile=open("newspaper.txt")
n=0
words=[]
counts=dict()
for line in myfile:
    word=line.split()
    for j in word:
        j=fix(j)#afero apo tin kathe leksi akira grammata
                #tou tipou " / . , kai kefalea grammata
        counts[j]=counts.get(j,0)+1
    n+=1
A=list(counts.values())
B=list(counts.keys())
A,B=sort(A,B)
print(" #  freq             word")
print("-------------------------")
for i in range(len(A)):
    print("%3d %5d %15s"%(i+1,A[i],B[i]))

