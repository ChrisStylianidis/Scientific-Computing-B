#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
a="$V_0(1-e^{-t/RC})$"
b="$V_0e^{-t/RC}$"

V0=12
R=1000
C=1E-6
Va=lambda x: V0*np.exp((-x)/(R*C))
Vf=lambda x: V0*(1-np.exp((-x)/(R*C)))
dt=0.0005
y=V0
t=0
ya=[]
ta=[]
while(y>0.12):
    ya.append(y)
    ta.append(t)
    t+=dt
    y=Va(t)
plt.plot(ta,ya,'r-',label=a)

y=0
t=0
yf=[]
tf=[]
while(y<(98/100)*V0):
    yf.append(y)
    tf.append(t)
    t+=dt
    y=Vf(t)
plt.plot(tf,yf,'k',label=b)
plt.grid(True)
plt.legend()
plt.show()
exit()
