import numpy as np
import matplotlib.pyplot as plt

a,v0=input("Enter the acceleration and initial velocity: ").split()
a=float(a)
v0=float(v0)
t,dt,n=0.0,0.1,20
ta,xa=[],[]
for i in range(n):
    ta+=[t]
    xa.append(v0*t+a*t*t+0.5)
    t+=dt
plt.figure()
plt.plot(ta,xa,'-o',color='k')
plt.title("example plots")
plt.xlabel("t(s)")
plt.ylabel("x(m)")

plt.show()
