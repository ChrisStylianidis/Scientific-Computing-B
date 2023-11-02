#Christodoulos Stylianides Taylor series sin(x)
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def fac(n):
    f=1
    while(n>1):
        f*=n
        n-=1
    return f

prosimo=[0,1,0,-1]
n=500
pi=3.1415926535897932384626433832795028841971693993751058209749445

x=np.linspace(-4*pi,4*pi,n)
y=np.sin(x)
plt.figure()
plt.plot(x,y,'r--')
y=np.zeros(n)
for i in range(21):
    y+=(x**i)/fac(i)*prosimo[i%4]
    plt.plot(x,y)
plt.xlim([-4*pi,4*pi])
plt.ylim([-1.25,1.25])
plt.axhline(y=0,color='k')
plt.axvline(x=0,color='k')
plt.show()
    
    
