#!/bin/python3
#Askisi 1

import numpy as np
import matplotlib.pyplot as plt

#creating
plt.figure()
plt.grid(True)
plt.xlabel("Position x(m)") 
plt.ylabel("Position y(m)") 
#plot

#-----------methodos euler------------
g,dt=9.8, 0.01
theta=20*np.pi/180
xpos,ypos,v0=0,0,500
vx=v0*np.cos(theta)
vy=v0*np.sin(theta)
xa,ya=[],[]
i=0
while(True):
    xa.append(xpos)
    #vx constant
    xpos+=vx*dt

    ya.append(ypos)
    vy-=9.8*dt
    ypos+=vy*dt
    if(ya[i-1]<0):
        xl=xpos
        break
    i+=1
plt.plot(xa,ya,"k",label="Euler")

#-----------theoritiki----------------
'''
y(t)=v0* sin* t-1/2gt^2, x(t)=v0 cos t
y(x)=tan*x-0.5*g*(x/(vo*cos))**2
'''
x=np.linspace(0,xl,100000)
y=np.tan(theta)*x-0.5*g*(x/(v0*np.cos(theta)))**2
plt.plot(x,y,'r--',label="Theory")


#-------methodos verlet speed---------

ntimes=i-1
h=0.01
m=1
x=np.zeros(ntimes)
x[0]=0
u=np.zeros(ntimes)
u[0]=500
for i in range(ntimes-1):
    uikaimiso=u[i]+(h*g)/(2*m)
    x[i+1]=x[i]+uikaimiso*h
    u[i+1]=uikaimiso+(h*g)/(2*m)
plt.plot(x,u,'g',label="Verlet")#lathos aksones



#plotting
plt.legend(loc="best")
plt.show()
