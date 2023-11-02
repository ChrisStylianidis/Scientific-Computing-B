#Askisi 5
#!/usr/root/python3

import numpy as np
import matplotlib.pyplot as plt
from random import seed, random, gauss

#ntries = int(input("How many tries? "))
ntries = 100000
seed(12345678)
x = []

for i in range(ntries):
    x.append(gauss(100,15))

cont,binv,intr=plt.hist(x,bins=50,range=(0.,200.),color='k',density=True,histtype='step')

plt.xlabel('x-values')
plt.ylabel('probability density function, (PDF)')
plt.title('Random number gaussian distributed')
plt.xlim(40,160)
plt.ylim(0.,0.03)
plt.text(60,0.025,r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.show()

