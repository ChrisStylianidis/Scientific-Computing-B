#!/bin/python3
'''
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
print("Hello World")

x=np.arange(-5,5,0.1)
y=x*x
z=x
plt.plot((x,y,z),'k')
plt.show()

APPLES = .50 
BREAD = 1.50 
CHEESE = 2.25 
numApples= 3
numBread= 4 
numCheese= 2 
prcApples= 3 * APPLES 
prcBread= 4 * BREAD 
prcCheese= 2 * CHEESE 
strApples= 'Apples' 
strBread= 'Bread'
strCheese= 'Cheese'
total = prcBread+ prcBread+ prcApples
print(f'{"My Grocery List":^38s}')
print(f'{"="*38}')
print(f'{strApples}\t{numApples:10d}\t\t${prcApples:>5.2f}')
print(f'{strBread}\t{numBread:10d}\t\t${prcBread:>5.2f}')
print(f'{strCheese}\t{numCheese:10d}\t\t${prcCheese:>5.2f}')
print(f'{"Total:":>19s}\t\t${total:>4.2f}')

class Polynomial:
    def __init__(self,lis):
        self.lis= lis
        
    def __str__(self):
        s=""
        if(len(self.lis)==0):
            return s
        if(self.lis[0]!=0):
            s+=str(self.lis[0])
        for i in range(1,len(self.lis)):
            if(self.lis[i]==0):
                continue
            if(self.lis[i]>0):
                s+="+"
            if(self.lis[i]==1):
                s+="(x^%d)"%(i)
            elif(self.lis[i]==-1):
                s+="-(x^%d)"%(i)
            else:
                s+="%d(x^%d)"%(self.lis[i],i)
        s=s.replace("^1","")
        return s
    def __add__(self,other):
        if(len(self.lis)>len(other.lis)):
            for i in range(len(other.lis)):
                self.lis[i]+=other.lis[i]
            return self
        else:
            for i in range(len(self.lis)):
                other.lis[i]+=self.lis[i]
            return other
    def __sub__(self,other):
        for i in range(len(other.lis)):
            other.lis[i]=-other.lis[i]
        if(len(self.lis)>len(other.lis)):
            for i in range(len(other.lis)):
                self.lis[i]+=other.lis[i]
            return self
        else:
            for i in range(len(self.lis)):
                other.lis[i]+=self.lis[i]
            return other
    def __mul__(self,other):
        new=Polynomial([])
        for i in range(len(other.lis)+len(self.lis)):
            new.lis+=[0]
        for i in range(len(self.lis)):
            for j in range(len(other.lis)):
                new.lis[int(i+j)]+=int(self.lis[i])*int(other.lis[j])
        return (new)
    def __call__(self,x):
        sum=0
        for i in range(len(self.lis)):
            sum+=self.lis[i]*(x**i)
        return sum
    def __deriv__(self):
        new=Polynomial([])
        for i in range(len(self.lis)-1):
            new.lis+=[0]
        for i in range(1,len(self.lis)):
            new.lis[i-1]=i*self.lis[i]
        return new
'''
from sympy import *
x,y=symbols('x y')
z=x*y
print(z)



'''

plt.plot(x,fs,'yellow',label="f(x)")
plt.plot(x,f1,'b',label="$f_1(x)$")
plt.plot(x,f5,'cyan',label="$f_5(x)$")
plt.plot(x,f10,'g',label="$f_{10}(x)$")
plt.plot(x,f100,'r',label="$f_{100}(x)$")
plt.legend()
plt.text(0.9,0.70,r'$f_{N} = ∑ \frac{2}{π}[1-(-1)^n]\frac{sin(nx)}{n}$',fontsize=12)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)

'''
