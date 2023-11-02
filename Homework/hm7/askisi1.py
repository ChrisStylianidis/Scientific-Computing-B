#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def simpson(f,a,b,dx):
    n=int((float(b-a)/dx)+1)#afou exw to dx vrisko tis fores tou loop
    s=0#to athrisma sum mou
    for i in range(0,n-2,2):#mexri to n-2 afou mesa sto loop exw i+2
        xa = a + i*dx
        xb = a + (i+1)*dx
        xc = a + (i+2)*dx
        s+=f(xa)+4*f(xb)+f(xc)#athrisma simpson
    s*=dx#epi dx/3
    s/=3
    return s#epistrefo tin timi tou athrismatos

def RK2(f,ft,ftt,a,b,dx):# f ft=(ftonos) ftt=(f tonos tonos)
    x=np.arange(a,b+dx,dx)#vrisko ton aksona ton x
    npoints=len(x)#to megethos einai ta npoints
    X=np.zeros(npoints)
    V=np.zeros(npoints)#megethos twn arrays
    X[0]=f(a)
    V[0]=ft(a)#arxikes times V einai i f tonos
    for i in range(npoints-1):
        Vmid = V[i] + 0.5*ftt(x[i])*dx
        X[i+1] = X[i] + Vmid*dx#vimata rk2
        V[i+1] = V[i] + ftt(x[i]+0.5)*dx
    plt.plot(x,X,'k',label="RK2")#sxediazo tin x,X
    y=f(x)#i theoritiki
    plt.plot(x,y,'r--',label="theory")#red me --
    s=0
    for i in range(0,len(X)-1):
        s+=(X[i+1]+X[i])*dx/2#ipologizo ta trapezia
    return s#epistrefo to athrisma
        
g=lambda x: 6*(x**3)#i g 
gt=lambda x: 18*x**2#i paragogos tis
gtt=lambda x: 36*x#i defteri paragogos tis g

#prints kai plots

print("Runge-Kutta 2nd order:",RK2(g,gt,gtt,5,8,0.15))
print("Simpson's:            ",simpson(g,5,8,0.15))#5206.5 (episis theoritiki)
print("Theory:                5206.5")

plt.grid(True)
plt.title("6x^3")
plt.legend(loc='best')
plt.show()
