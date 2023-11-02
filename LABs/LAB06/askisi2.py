#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

myfunc=lambda x: np.exp(-x)*np.cos(2*np.pi*x)
f=lambda x: np.cos(2*np.pi*x)

x1=np.arange(0,5.0,0.1)
x2=np.arange(0,5.0,0.02)

plt.subplot(211)
plt.grid(True)
plt.text(2,0.2,r'f(x) = $e^{-x}cos(2πx)$')
plt.xlabel("x")
plt.ylabel("myfunc")
plt.plot(x1,myfunc(x1),'b.')
plt.plot(x2,myfunc(x2),'g--')

plt.subplot(212)
plt.ylabel('f(x) = $e^{-x}cos(2πx)$')
plt.xlabel("x")
plt.grid(True)
plt.plot(x2,f(x2),'r--')
plt.show()
exit()
