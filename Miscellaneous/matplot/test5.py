#Christodoulos Stylianides Askisi 3
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
n=50
x=np.linspace(-n,n,n**2)
y=np.zeros(n**2)
plt.plot(x,y,'k')
x=np.linspace(-2500,2500,n**2)
plt.plot(y,x,'k')
x=np.linspace(-n,n,n**2)
y=x**2
plt.plot(x,y,'r')
x=np.linspace(-(n)/3.5,(n)/3.5,n**2)
y=x**3
plt.plot(x,y,'g')
plt.show()


exit()
