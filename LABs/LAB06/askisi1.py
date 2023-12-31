#Christodoulos Stylianides 1065882
#!/bin/python3

import numpy as np
import matplotlib.pyplot as ptl
func1=lambda x:4*np.exp(-2*x)
func2=lambda x: 0.5*x**2
x=np.arange(0.,2.1,0.1)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,func1(x),'r-')
plt.plot(x,func2(x),'b--')
plt.text(0.4,2.0,r'f(x)=$4e^{-2x}$')
plt.text(1.5,1.0,r'f(x) = $0.5x^2$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(x,func1(x)-func2(x),'b-')
plt.text(0.5,1.5,r'f(x) = $4e^{-2x} -0.5x{^2}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0,2)
plt.grid(True)
plt.axhline(y=0,color='red',linestyle='--')
plt.tight_layout() 
plt.show()
