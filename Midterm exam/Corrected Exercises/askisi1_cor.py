#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

f=lambda x: (x**2)*np.exp(-x)#f(x)=x^2*e^-x

def fp1(x,dx):
    return (f(x+dx)-f(x-dx))/(2*dx)
def fp2(x,dx):
    return (f(x+dx)-f(x))/(dx)#orizo tis fp1 fp2
ftonos3=-3*np.exp(-3)#f'(3) i kanoniki timi

deltax=[]
for n in range(1,51):
    deltax+=[2**(-n)]#ipologizo tis times tou dx gia to a
x=3#x0=3
e1=[]
for dx in deltax:
    e1+=[abs(fp1(x,dx)-ftonos3)]#ipologizo tin timi tis e^(1)
e2=[]

for dx in deltax:
    e2+=[abs(fp2(x,dx)-ftonos3)]#e^(2)

deriv=np.zeros(3)
deriv[0]=fp1(3,0.1)
deriv[1]=fp1(3,0.05)
deriv[2]=fp1(3,0.025)#o array deriv gia to b erotima
dx=[0.1,0.05,0.025]

p=np.polyfit(dx,deriv,2)#to p exei tora tis times gia to polionimo
print("P =",p)
 
y=p[0]*(3**2)+p[1]*3+p[2]      #<<< To fit einai paragwgos sto x=3 ws pros to dx. Ara y = p[0]*dx**2 + p[1]*dx+p[2] 
ytonos=6*p[0]+p[1]             #<<< kai to ytonos einai to ftonos3
print("y\'=",ytonos)
print("y\'-f'(3)=",ytonos-ftonos3)

#=============================
#<< Ayto pou xreiazontan na ginei sto simeio ayto einai
#<< na upologistei to sfalma tis paragwgou gia dx=0.
#>> Apo to poluwnumo tou fit: p2*dx^2+p1*dx+p0 gia dx=0 exoume oti i
#>> timi tis paragwgou (to fit einai ektimomeni paragwgos ws pros dx) gia
#>> dx=0 einai p0. Epomenws to sfalma me tin pragmatiki timi tis paragwgou eini
#>> p0-ftonos3(x0).
#>> To sfalma sto dx=0.025 tha itan p2*(0.025)**2+p1*(0.025)+p0 - ftonos3
#=============================


plt.grid(True)
plt.plot(deltax,e1,"k",label="e1")                #<<<< Den einai logarithmiko to grafima
plt.plot(deltax,e2,"r",label="e2")#alfa erotima
plt.loglog       
plt.legend()
plt.show()#den to prolava olo (xronos)

#===========================
# sxolia:             1/1
# compilation:        3/3
# algorithmos:        5/6
#===========================
# (a) meros:          9/10
#===========================
# (b) meros:          2/6
#===========================
# (c) meros:          0/4
#===========================
# Sunolo:            11/20
#===========================
