#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
def f(n,x):
    sum=0
    for i in range(1,n+1):
        sum+=(2*np.sin(i*x)/(np.pi*i))*(1-((-1)**i))
    return sum

def fk(x):
    ans=np.ones(len(x))
    for i in range(len(x)):
        if x[i]<0 and x[i]>=-np.pi:
            ans[i]=-1
    return ans
myfile=open("fourier.dat","w")
x=np.arange(0,np.pi,np.pi/500)
fs=fk(x)
f1=f(1,x)
f5=f(5,x)
f10=f(10,x)
f100=f(100,x)

print(" {0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {5:10s}".format("x:","f(x):","f1(x):","f5(x):","f10(x):","f100(x):"))
myfile.write(" {0:10s} {1:10s} {2:10s} {3:10s} {4:10s} {5:10s}".format("x:","f(x):","f1(x):","f5(x):","f10(x):","f100(x):\n"))
for i in range(len(x)):
    print("{0:8.5f} {1:10.5f} {2:10.5f} {3:10.5f} {4:10.5f} {5:10.5f}".format(x[i],fs[i],f1[i],f5[i],f10[i],f100[i]))
    myfile.write("{0:8.5f} {1:10.5f} {2:10.5f} {3:10.5f} {4:10.5f} {5:10.5f}\n".format(x[i],fs[i],f1[i],f5[i],f10[i],f100[i]))

plt.plot(x,fs,'yellow',label="f(x)")
plt.plot(x,f1,'b',label="$f_1(x)$")
plt.plot(x,f5,'cyan',label="$f_5(x)$")
plt.plot(x,f10,'g',label="$f_{10}(x)$")
plt.plot(x,f100,'r',label="$f_{100}(x)$")
plt.legend()
plt.text(0.9,0.70,r'$f_{N} = ∑ \frac{2}{π}[1-(-1)^n]\frac{sin(nx)}{n}$',fontsize=12)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.savefig("hm2_prob3.pdf")
plt.show()
exit()


#check ===================
#1) sxolia:         0/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                9/10
