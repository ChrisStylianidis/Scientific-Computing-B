#Christodoulos Stylianides 1065882
#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

m=0.01
D=0.01
v0=50
'''
i provlepsi mou einai oti to tanodou tha einai pio mikro apo to tkathodou
afou xoris antistasi stin epistrofi tou tha eixe idia taxitita me tin arxiki
alla afou iparxei antistasi den tha exei tin idia taxitita stin epistrofi
ara tha xriastei perissotero xrono apo to megisto simio sto edafos
anti apo to edafos sto megisto simio
tanodou<tkathodou

Fant=-mDu^2
F=Fant+Fb
F=-mDu^2-mg
mdudt=-mDu^2-mg
dudt=-Du^2-g
'''
def dudt(t,u):
    return v0-D*u*u-9.8

def rungeKutta(x0,y0,x,h,what):#i metavliti what einai bool se periptosi
    n=(int)((x-x0)/h)#pou thelw na epistrepso x i y
    y=y0
    for i in range(1,n+1):
        
        k1 = h * dudt(x0,y)
        k2 = h * dudt(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dudt(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dudt(x0 + h, y + k3)
        y += (1.0/6.0)*(k1+2*k2+2*k3+k4)
        if(abs(dudt(x0+h,y))<1e-4) and what==True:#an midenistei to dudt
            return x0#epistrefo ton xrono
        x0+= h
    return y
tanodou=(rungeKutta(0,v0,100,0.01,True))
tkathodou=(rungeKutta(tanodou+0.01,0,100,0.01,True))-tanodou
#o xronos kathodou einai apo ton xrono anodou mexri to edafos
print("xronos anodou:",tanodou)
print("xronos kathodou:",tkathodou)
#SF=-mDu^2-mg
print("Maximum Height:",rungeKutta(tanodou-0.01,0,tanodou+0.01,0.01,True))
V=np.linspace(0,25,1000)
SF=-m*(D*V*V+9.8)
plt.grid(True)
plt.title("SF=-mDu^2-mg")
plt.xlabel("V (m/s)")
plt.ylabel("SF (N)")
plt.plot(V,SF,'k')
plt.show()
plt.savefig("Stone.pdf")
#clearly something is wrong...
    
#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 5/6    
#=========================
#Sum                9/10
