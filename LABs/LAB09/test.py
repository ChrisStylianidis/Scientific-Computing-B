#dialeksis teest
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation 

fig=plt.figure()
ax=plt.axes(xlim=(0,2),ylim=(-2,2))
line,=ax.plot([],[],lw=2)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    x=np.linspace(0,2,1000)
    y=np.sin(2 * np.pi * (x-0.01*i))
    line.set_data(x,y)
    return line,
anim = animation.FuncAnimation(fig,animate,init_func=init,frames=200,interval=20,blit=True)
anim.save('basic.gif',fps=2)
plt.grid(True)
plt.show()
