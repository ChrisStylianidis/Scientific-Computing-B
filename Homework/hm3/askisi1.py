#Christodoulos Stylianides Askisi 1 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

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

myfile=open("inp_integers.dat")
counts=dict()
n=0
for line in myfile:
    x=line.split()
    for j in x:
        counts[j]=counts.get(j,0)+1
    n+=1
A=list(counts.values())
B=list(counts.keys())
A,B=sort(A,B)
print("  #  freq    number")
print("-------------------")
for i in range(len(A)):
    print("%3d %5d %9s"%(i+1,A[i],B[i]))
x=np.arange(1,31)
y=np.zeros(30)
for i in range(len(x)):
    y[i]=counts[str(x[i])]
    
plt.grid(True)
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.plot(x,y,'k')
plt.show()
