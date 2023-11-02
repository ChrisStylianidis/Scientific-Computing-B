#Christodoulos Stylianides 1065882
#!/bin/python3

from numpy import sqrt
import matplotlib.pyplot as plt
from sympy import *

f1=lambda x: x**2
f2=lambda x: sqrt(x)

def trapez(f,a,b,n):
    dx = (b-a)/float(n)#evros upodiastimaton (n arithmos upodiastimaton)
                       #a kai b oria oloklirosis
    s = 0.5*(f(a)+f(b))#i proti timi
    for i in range(1,n):
        s = s + f(a+i*dx)#i timi tis sinartisis sta endiamsesa
    return dx*s

def midpoint(f,a,b,n):
    dx = float(b-a)/n#evresi upodiastimaton
    result = 0#arxikopoiisi tou sum
    for i in range(n):
        result += f((a + dx/2.0) + i*dx)#i timi sto kathe diastima
    result *= dx
    return result


def olokl(f,xlow,xup,eps,method):
    n=10
    x=Symbol('x')
    xp,yp=[],[]
    yp.append(n)
    if method=='t':
        proto=trapez(f,xlow,xup,2*n)
        deftero=trapez(f,xlow,xup,n)
        xp.append(abs(proto-deftero))
        while(abs(proto-deftero)>eps):
            n=(2*n)
            proto=trapez(f,xlow,xup,2*n)
            deftero=trapez(f,xlow,xup,n)
            yp.append(n)
            xp.append(abs(proto-deftero))
        return proto,float(integrate(f(x),(x,xlow,xup))),xp,yp

    elif method=='m':
        proto=midpoint(f,xlow,xup,2*n)
        deftero=midpoint(f,xlow,xup,n)
        xp.append(abs(proto-deftero))
        while(abs(proto-deftero)>eps):
            n=(2*n)
            proto=midpoint(f,xlow,xup,2*n)
            deftero=midpoint(f,xlow,xup,n)
            yp.append(n)
            xp.append(abs(proto-deftero))
        return proto,float(integrate(f(x),(x,xlow,xup))),xp,yp
    else:
        print("Error, method must be trapezoid(t) or midpoint(m)")
    
        
value,theory,xplot,yplot=olokl(f2,0,2,10e-6,'m')
plt.plot(xplot,yplot)
plt.show()
#print("0.00000000001")
print(abs(theory-value))
