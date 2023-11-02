#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

lista=[]
myfile=open("inp_integers.dat")
for line in myfile:
    x=line.split('\n')
    lista+=[int(x[0])]
myfile.close()
y=np.zeros(31)
for i in lista:
    y[i]+=1
y=y[1:]
x=np.arange(1,31)

plt.title("Random Numbers")
plt.xlabel("Integer")
plt.ylabel("Frequency")
plt.plot(x,y,'k--')
plt.show()
