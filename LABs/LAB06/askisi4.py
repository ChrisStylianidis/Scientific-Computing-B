#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
rad=lambda x: x*np.pi/180

u0=22
y0=25
theta=30
dt=0.1
y=[]
t=[]
ycurr=0
tcurr=0
while(ycurr>=0):
    ycurr=y0+u0*np.sin(rad(theta))*tcurr-0.5*9.81*(tcurr**2)
    if(ycurr>0):
        y.append(ycurr)
        t.append(tcurr)
    tcurr+=dt
plt.plot(t,y,'k')
plt.grid(True)
plt.ylabel("Height")
plt.xlabel("Time")

plt.show()
