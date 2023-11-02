#Askisi 3 Christodoulos Stylianides 1065882
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
    n=2#ksekino tin methodo me n=2 anti me ena megalo n kai na diero
    x=Symbol('x')#to symbol to xrisimopoio gia theoritiki lisi tou oloklir.
    xp,yp=[],[]#oi pinakes gia to (c) erotima
    yp.append(n)#i proti timi tou y aksona
    if method=='t':#i methodos gia to trapezio
        proto=trapez(f,xlow,xup,2*n)#onomazo tin metavliti proto gia na 
        deftero=trapez(f,xlow,xup,n)#afero to proto-deftero (den exei simasia)
        xp.append(abs(proto-deftero))#i proti timi tou x aksona
        while(abs(proto-deftero)>eps):#oso i diafora tous einai megaliteri tis 
            n=(2*n)#akrivias, afksano ta diastimata
            proto=trapez(f,xlow,xup,2*n)
            deftero=trapez(f,xlow,xup,n)#ksana ipologizo tis times
            yp.append(n)#appends stous pinakes pou epistrefo gia plots
            xp.append(abs(proto-deftero))
        return proto,float(integrate(f(x),(x,xlow,xup))),xp,yp
    elif method=='m':#methodos midpoint pou akolouthei akrivos tin idia
        proto=midpoint(f,xlow,xup,2*n)#diadikasia me tin trapezium
        deftero=midpoint(f,xlow,xup,n)
        xp.append(abs(proto-deftero))
        while(abs(proto-deftero)>eps):
            n=(2*n)
            proto=midpoint(f,xlow,xup,2*n)
            deftero=midpoint(f,xlow,xup,n)
            yp.append(n)
            xp.append(abs(proto-deftero))
        return proto,float(integrate(f(x),(x,xlow,xup))),xp,yp
    else:#se periptosi lathous i sinartisi epistrefei error
        print("Error, method must be trapezoid(t) or midpoint(m)")
        return

value,theory,xplot,yplot=olokl(f1,0,2,0.1,'t')#kalo tin proti sinartisi, x**2
plt.plot(xplot,yplot,'ko',label="x^2")#plots apo tin sinartisi
plt.plot(xplot,yplot,'k--')#diakekomena mavra kai kiklous gia na einai pio katharo
print("The numerical value is: %.4f"%value)#i numerical apantisi
print("The actual error between the numerical answer\nand the true value for the integration of x^2 is %f"%(abs(theory-value)))#i pragmatiki diafora tous

plt.xlabel("Precision")#plots
plt.ylabel("Number of subspaces")
plt.grid(True)
plt.legend()
print("------------------------------------------")#diaxoristiki grammi
plt.figure()#kainourio plot giati tis rizas x tha einai loglog
value,theory,xplot,yplot=olokl(f2,0,2,10e-10,'m')#einai poli mikri akrivia 
plt.plot(xplot,yplot,'go',label="√x")#giafto kathisterei to programma
plt.plot(xplot,yplot,'g--')#ta ipolipa prints einai ta idia kai ta plots idio 
print("The numerical value is: %.10f"%value)#skeptiko me tis eksisosis x**2
print("The actual error between the numerical answer\nand the true value for the integration of √x is %f"%(abs(theory-value)))

plt.xlabel("Precision")
plt.ylabel("Number of subspaces")
plt.grid(True)
plt.loglog()
plt.legend()


plt.show()
exit()


#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10
