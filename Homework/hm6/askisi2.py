#Christodoulos Stylianides 1065882
#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

#dx/dt=u    du/dt=4-0.5u

def dudt(x,u):
    return 4-0.5*u#i diaforiki eksisosi gia to dudt

def rk2(x0,v0,dt):#rungekutta2ou vathmou
    tfinal=100#theoro ws final to 100 (den ginete to plot mexri to 100)
    t=np.arange(0,tfinal+dt,dt)#+dt gia na exei kai tin timi tou 100
    npoints=len(t)#to megethos ton arrays pou tha dimiourgithon
    X=np.zeros(npoints)
    V=np.zeros(npoints)#midenizo tous pinakes
    X[0]=x0
    V[0]=v0#arxikopoio tis protes theseis
    for i in range(npoints-1):#mexri to n-1 giati sto for xrisimopoio i+1
        Vmid=V[i] + dudt(X[i],V[i])*dt#ipologizo tin mesi timi tis taxititas
        X[i+1] = X[i] + Vmid*dt #ipologizo to x
        V[i+1] = V[i] + dudt(X[i]+1/2,V[i]+1/2)*dt#kai to v
    Vmax=V[len(V)-1]#krato ws to vmegisto tin teleftea timi tou array
    return X,V,Vmax#epistrefo afta pou thelw

x0=float(input("Give value for initial position: "))
v0=float(input("Give value for initial velocity: "))
dt=float(input("Give value for dt: "))#zitaw arxikopoiiseis apo xristi

x,v,vmax=rk2(x0,v0,dt)#run tin function
newx,newv=[],[]
time=[]#ta lists gia to 99%

utheory,xtheory=[],[]

for i in range(len(x)):
    if(v[i]<0.99*vmax):#mexri na vrw timi 99%tou vmax dimiourgo listes
        newx.append(x[i])
        newv.append(v[i])
        t=i*dt
        time.append(t)#anti na exw metavliti t+=dt vazo i*dt
        utheory.append(8+(v0-8)*np.exp(-0.5*t))
        xtheory.append(8*t+np.exp(-0.5*t)*(16-2*v0)+x0-16+2*v0)
    else:
        break#vgeno apo to loop molis teleiwsw

plt.subplot(122)#position
plt.grid(True)
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.plot(time,xtheory,'r--',label="Theory")
plt.plot(time,newx,'k',label="Position")
plt.legend(loc='best')
plt.title("dx/dt=u")

plt.subplot(121)#velocity
plt.plot(time,utheory,'r--',label="Theory")
plt.grid(True)
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.plot(time,newv,'k',label="Velocity")
plt.legend(loc='best')
plt.title("du/dt=4-0.5u")
plt.savefig("AirResistance_plot1.pdf")

#du/dt=4-0.5u
'''
du/dt+0.5u=4
oloklirotikos paragontas=e^(oloklr0.5dt)=e^0.5t
e^(0.5t)*u=olokl(4e^0.5t)+c, opou c=v0-8
u=8+(v0-8)*e^(-0.5t)
afou u=dx/dt
dx=(8+(v0-8)*e^(-0.5t))dt
x=8*t+np.exp(-0.5*t)*(16-2*v0)+c, opou c=x0-16+2*v0
'''

plt.figure()

plt.subplot(121)#velocity
plt.grid(True)
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
errorv=[]
for i in range(1,len(newv)):
    errorv.append(abs((utheory[i]-newv[i])/newv[i]))
plt.plot(time[1:],errorv,'g',label="VelocityError")
plt.legend(loc='best')
plt.title("Percent Error (Velocity)")

plt.subplot(122)#position
plt.grid(True)
plt.xlabel("t(s)")
plt.ylabel("x(m)")
errorp=[]
for i in range(1,len(newx)):#o logos pou ksekino apo to 1 einai epd i proti timi einai 0 ara tin agnoo
    errorp.append(abs(((xtheory[i]-newx[i])/newx[i])))#(theory-pr)/pr
plt.plot(time[1:],errorp,'g',label="PositionError")#o logos pou ksekinao apo to 1 kai oxi apo to 0 einai epd sto for ksekinisa apo to 1 gia na apofigo to /0
plt.legend(loc='best')
plt.title("Percent Error (Position)")
plt.savefig("AirResistance_plot2.pdf")#saving fig

plt.show()#show
