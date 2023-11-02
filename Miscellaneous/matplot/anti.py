#Askisi antistasis
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

dt=0.25
v0 = 700
theta = (55*np.pi)/180
A_m= 4E-5
x,y= [],[]
x.append(0)
y.append(0)

xpos=0.0
ypos=0.0

vx= v0* np.cos(theta)
vy= v0* np.sin(theta)
istep= 0
doit=True
while doit:
    f = A_m*np.sqrt(vx**2 + vy**2)#dragforce
    vy= vy-9.8 * dt-f * vy* dt
    vx= vx-f * vx* dt
    xpos+=vx*dt
    ypos+=vy*dt
    x.append(xpos)#Euler-Cromer
    y.append(ypos)
    istep+=1
    
    if y[istep]<= 0.0:
        doit=False #vlima ktipise sto edafos 
nstep= istep
slope=(y[nstep]-y[nstep-1])/(x[nstep]-x[nstep-1])
x[nstep]= (x[nstep-1]- y[nstep-1]/slope)
y[nstep]= 0
t=0.1
vges=True
xnd,ynd=[],[]
while(vges):
    xedw=v0*t*np.cos(theta)
    yedw=v0*t*np.sin(theta)-0.5*9.8*(t**2)
    print(yedw)
    xnd.append(xedw)
    ynd.append(yedw)
    if yedw<=0.0:
        vges=False
    t+=0.1
plt.plot(xnd,ynd,'r--')
plt.plot(x,y,'k')

plt.show()
