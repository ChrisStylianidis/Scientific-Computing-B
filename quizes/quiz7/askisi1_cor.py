#Quiz 7 Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
'''
a) P=Fu
P=m a u
P/m=a*u => a=P/(m*u) (epitaxinsi)        #<<<< (4/4)
(P/m)*t=u^2/2
2t(P/m)=u^2
u=(2tP/m)^(1/2) (taxitita)
'''

#b)
dt=0.1
m=70
v0=4
P=400
t=0
u=v0
a=P/(m*dt)            #<<< P/(m*u)      (1/4)
while(t<3600):
    u+=a*dt           #<<< H epitaxunsi den einai statheri alla eksartatai apo
    t+=dt             #>>> tin taxutita. H entoli ayti den apotelei vima
                      #>>> EulerCrommer
print("my ans:",np.sqrt(u))
print("theory:",np.sqrt(2*3600*P/m))

#c)
'''
F=P/u-DApu^2
ma=P/u-DApu^2
a=P/(m*u)-DApu^2/m                     (3/3)
'''
#d)
D=0.45
A=0.33
p=1.204
dt=0.1
t=np.arange(0,3600+dt,dt)
npoints=len(t)
V=np.zeros(npoints)
V[0]=v0
def a(u):
    return P/(m * u)-D*A*p*u*u/m         (3/4)
for i in range(npoints-1):
    Vmid=V[i]+0.5*a(V[i])*dt
    V[i+1]=V[i]+a(V[i]+0.5)*dt     #<< V[i]+0.5???  Se ti monades ?
print("With the drag force the cyclist has v=%f m/s"%V[npoints-1])

#========
#  11/15
#========
