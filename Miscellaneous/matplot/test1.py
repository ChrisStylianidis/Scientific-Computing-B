import numpy as np
import matplotlib.pyplot as plt
n=50
m=2
ma=5
x=np.linspace(m,ma,n)
for i in range(2,4):
    y=x**i
    plt.plot(x,y)
plt.ylim((0,100))
plt.show()
exit()
