#Christodoulos Stylianides Askisi 3 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def trapezium(f,a,b,dx):
    n=int((b-a)/dx)
    s = 0.5*(f(a)+f(b))
    for i in range(1,n):
        s += f(a + i*dx)
    return dx*s

dt=0.05
t=np.arange(0,(2)*np.pi+dt,dt)#i sinartisi ekrigniete kai ftanei to +apeiro
#giafto to perno mexri ta 2misi pi

X=np.zeros(len(t))
V=np.zeros(len(t))
A=np.zeros(len(t))

X[0]=0.0
V[0]=1.0
A[0]=0.0
bool=True
value=0.0001
for i in range(len(t)-1):

    if abs(V[i])<0.1 and not(bool):
        holdb=t[i]
        print("Solution at:",holdb)
        if abs((c+1)*(holda)-holdb)>0.01:
            print("dt reduced by %.4f"%value)
            dt-=value
        c+=1

    if abs(V[i])<0.1 and bool:
        c=1
        bool=False
        holda=t[i]
        print("First Solution at:",holda)
        dt-=value
    X[i+1]=X[i]+V[i]*dt+0.5*A[i]*dt**2
    V[i+1]=V[i]+A[i]*dt
    A[i+1]=(-4)*float(X[i]**3)

plt.grid(True)
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.plot(t,X,'k--')

plt.figure()
plt.grid(True)
plt.ylabel("x(m)")
plt.xlabel("v(m/s)")
plt.plot(V,X,'k-')
plt.show()

## check, ateliwto, lipun arketa kommatia
## des tin lisi
#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 3/6    
#=========================
#Sum                7/10

