#Christodoulos Stylianides 1065882
#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

cosh=lambda x: 0.5*(np.exp(x)+np.exp(-x))
sinh=lambda x: 0.5*(np.exp(x)-np.exp(-x))
#kanonika eprepe na ta xrisimopoio apo numpy apefthias alla ekana ta dika mou

def f(x):
    return -9*sinh(x)#i paragogos einai 9sinh(x) ara i F einai -9sinh(x)

def verlet(v0,m,size,x0=0,h=0.1):
    u=np.zeros(size)
    x=np.zeros(size)
    u[0]=v0
    x[0]=x0
    for i in range(size-1):#ena for gia na gemiso tous pinakes me tis times
        ukmiso=u[i]+h*f(x[i])/(2*m)
        x[i+1]=x[i]+ukmiso*h
        u[i+1]=ukmiso+h*f(x[i+1])/(2*m)#ipologismos me vasi tous tipous 
    return x,u
v01=5
v02=-10#arxikes times taxititwn gia ta dio somatidia
#mazes:
m1=float(input("Give mass for particle 1: "))
m2=float(input("Give mass for particle 2: "))
dt=9.76563e-05
tmax=0.01#den akoloutho to orio tou paradigmatos
'''
me ena toso mikro dt mou emfanizei sto plot ena prasino kouti
epidi einai simpiesmeni i grafiki tou hmitonou/sinimitonou
giafto elaxistopoio to tmax afou idi simvainei na sinantontai ta particles
polles fores se xrono ligotero tou 0.01
'''
time=np.arange(0,tmax,dt)

newx1,newy1=verlet(5,m1,len(time))
newx2,newy2=verlet(-10,m2,len(time))#kalw tis sinartiseis gia ta dio particles

plt.title("Particles")
plt.xlabel("Time t(s)")
plt.ylabel("Position x(m)")
plt.grid(True)
plt.plot(time,newx1,"k",label="Particle1")
plt.plot(time,newx2,"g",label="Particle2")
plt.legend(loc="best")#graphing and saving
plt.savefig("Particles.pdf")

newx=newx1-newx2#i sinartisi stin opia prepei na vro to y=0
for i in range(1,len(newx)-1):
    if (newx[i])*(newx[i+1])<0:
        #tha dimiourgiso mia afthia me ta simia afta kai vazo y=0
        #ara vrisko to x kai krataw tin thesi se ena position
        y1=newx[i]
        y2=newx[i+1]
        x1=time[i]
        x2=time[i+1]
        klisi=(y2-y1)/(x2-x1)
        x=-y1/klisi+x1
        position=i
        break#break gia na vrisko tin proti fora pou vrethontai kai oxi tin teleftea
print("At t=%.15fs the particles will be:\n %.15fm away from starting point"%(x,(newx1[position]+newx1[position+1])/2))

plt.show()
#i thesi pou tha vrethoun ta somatidia einai
#(i mazes theorisa oti einai 1 kai gia ta dio somatidia)
#x=0.756056624968324m ston xrono
#t=0.000762330919783s

#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10
