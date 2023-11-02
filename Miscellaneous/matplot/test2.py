import numpy as np
import matplotlib.pyplot as plt
def fac(n):
    f=1
    while n>1:
        f*=n
        n-=1
    return f



n=500
m=-5
ma=5
x=np.linspace(m,ma,n)
y=np.cos(x)
y1=1-0.5*x*x
z=y1+(x**4)/fac(4)
plt.plot(x,y,'black',linestyle='--')
plt.plot(x,z,'r',x,y1,'g')
#plt.plot(x,y1,'g')
plt.title("example plots")
plt.xlabel("Input")
plt.ylabel("Values")


plt.show()
exit()
