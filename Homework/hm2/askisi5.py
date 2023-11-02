#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt



myfile=open("FitMeasurements.dat","w")
readme=open("Measurements.txt","r")
a,m,l=np.loadtxt(readme,unpack=True,skiprows=1)


msqr=0
mone=0
mult=0
N=len(a)
for i in range(N):
    msqr+=m[i]*m[i]
    mone+=m[i]
    mult+=m[i]*l[i]
mone*=mone
D=N*msqr-mone
A=msqr*l.sum()-m.sum()*mult
A/=D
B=N*mult-m.sum()*l.sum()
B/=D

sl=0
for i in range(N):
    sl+=(l[i]-A-B*m[i])**2
sl/=(N-2)
sl=np.sqrt(sl)
sa=sl*np.sqrt(msqr/D)
sb=sl*np.sqrt(N/D)
#A=38.990 kai B=2.055
#sl=1.19262
#(A+-)sa=1.25083
#(B+-)sb=0.18857
myfile.write("A=%.3f +- %.5f\nB=%.3f +- %.5f"%(A,sa,B,sb))
