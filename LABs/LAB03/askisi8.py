#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2+2*x+1

A=[]
x=[]
myfile=open('lab03_askisi8.txt','w')
myfile.write("x:\tf(x):\n")
for i in range(-20,21):
    A+=[f(i)]
    x+=[i]
    myfile.write("{0:5d} {1:7d}\n".format(i,f(i)))
myfile.close()
plt.grid(True)
plt.title("$f(x)=x^2+2x+1$")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,A,'k')
plt.show()
exit()
