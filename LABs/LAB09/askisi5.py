#dialeksis teest
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation 

fig=plt.figure()
L=2.2
ax=plt.axis([-L/2,L/2,-L/2,L/2])
line,=plt.plot([],[],'ko')


def animate(i):
    x=np.cos(i)
    y=np.sin(i)
    line.set_data(x,y)
    return line,
fram=np.linspace(0,2*np.pi,90)
anim = animation.FuncAnimation(fig,animate,frames=fram,blit=True,repeat=True)
#anim.save('basic.gif',fps=30)
plt.grid(True)
plt.show()

