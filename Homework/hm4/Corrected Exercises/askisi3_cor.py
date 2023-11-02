#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np

def min(a,b):
    if a>b:
        return b
    return a
def max(a,b):
    if a>b:
        return a
    return b


class MyLimits:
    def __init__(self,a,b):
        #constructor
        self.a= a
        self.b= b
    def __str__(self):
        return "[%5.2f , %5.2f]"%(self.a,self.b)
    def __add__(self,other):
        return MyLimits(self.a+other.a,self.b+other.b)
    def __sub__(self,other):
        return MyLimits(self.a-other.a,self.b-other.b)
    def __mul__(self,other):
        a=self.a
        b=self.b
        c=other.a
        d=other.b
        return MyLimits(min(min(a*c,a*d),min(b*c,b*d)),max(max(a*c,a*d),max(b*c,b*d)))
    def mul(self,k):
        return MyLimits(k*self.a,k*self.b)
    def __truediv__(self,other):
        a=self.a
        b=self.b
        c=other.a
        d=other.b
        return MyLimits(min(min(a/c,a/d),min(b/c,b/d)),max(max(a/c,a/d),max(b/c,b/d)))

Tm=0.45
T=MyLimits(Tm*0.95,Tm*1.05)
y0=MyLimits(0.99,1.01)

g=(y0.mul(2))/(T*T)
print("g = 2yℴt¯² =",g)#A erotima

Rm=6
R=MyLimits(0.9*Rm,1.1*Rm)
oros=(4*np.pi)/3
V=R.mul(oros)*R*R
print("𝑉 = (4πR³)/3=",V)#B erotima
exit()

#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10
