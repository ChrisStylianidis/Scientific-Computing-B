#Christodoulos Stylianides 1065882
#Askisi 5
#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def dndt(t,n):
    return a*n-b*n*n 

def ruK4(x0,y0,x,h):
    n=(int)((x-x0)/h)
    y=[]
    y.append(y0)
    yp=y0
    for i in range(1,n+1):
        k1 = h * dndt(x0,yp)
        k2 = h * dndt(x0 + 0.5 * h, yp + 0.5 * k1)
        k3 = h * dndt(x0 + 0.5 * h, yp + 0.5 * k2)
        k4 = h * dndt(x0 + h, yp + k3)
        yp= (1.0/6.0)*(k1+2*k2+2*k3+k4)
        y.append(yp)
        x0+= h
    return y,len(y)
def theory(dt,N0):#den vazo a b giati tha kaleso tis sinartiseis meta ton orismo tous
    N=(N0*a*np.exp(a*dt)/(a-b*N0+b*N0*np.exp(a*dt)))
    plt.plot(dt,N,'r--',label="Theory")

#alpha
plt.title("(a) a=10 b=3 N(0)=10")
plt.xlabel("t(months)")
plt.ylabel("N(#)")
plt.grid(True)
a=10
b=3
n,le=(ruK4(0,10,10,0.1))
dt=np.linspace(0,10,le)
theory(dt,10)
plt.plot(dt,n)
#alpha

#beta

plt.figure()
plt.title("(b) a=10 b=0.01 N(0)=1000")
plt.xlabel("t(months)")
plt.ylabel("N(#)")
plt.grid(True)
a=10
b=0.01
dt=np.linspace(0,10,1000)
n,le=(ruK4(0,1000,10,0.1))
dt=np.linspace(0,10,le)
theory(dt,1000)
plt.plot(dt,n)

#beta
plt.show()
