#Christodoulos Stylianides 1065882
#!/bin/python3

def min(a,b):
    if a<b:
        return a
    return b

class Polynomial:
    def __init__(self,lis):
        self.lis= lis
    def __str__(self):
        s=""
        if(len(self.lis)==0):
            return s
        if(self.lis[0]!=0):
            s+=str(self.lis[0])
        for i in range(1,len(self.lis)):
            if(self.lis[i]==0):
                continue
            if(self.lis[i]>0):
                s+="+"
            if(self.lis[i]==1):
                s+="(x^%d)"%(i)
            elif(self.lis[i]==-1):
                s+="-(x^%d)"%(i)
            else:
                s+="%d(x^%d)"%(self.lis[i],i)
        s=s.replace("^1","")
        return s
    def __add__(self,other):
        if(len(self.lis)>len(other.lis)):
            for i in range(len(other.lis)):
                self.lis[i]+=other.lis[i]
            return self
        else:
            for i in range(len(self.lis)):
                other.lis[i]+=self.lis[i]
            return other
    def __sub__(self,other):
        for i in range(len(other.lis)):
            other.lis[i]=-other.lis[i]
        if(len(self.lis)>len(other.lis)):
            for i in range(len(other.lis)):
                self.lis[i]+=other.lis[i]
            return self
        else:
            for i in range(len(self.lis)):
                other.lis[i]+=self.lis[i]
            return other
    def __mul__(self,other):
        new=Polynomial([])
        for i in range(len(other.lis)+len(self.lis)):
            new.lis+=[0]
        for i in range(len(self.lis)):
            for j in range(len(other.lis)):
                new.lis[int(i+j)]+=int(self.lis[i])*int(other.lis[j])
        return (new)
    def __call__(self,x):
        sum=0
        for i in range(len(self.lis)):
            sum+=self.lis[i]*(x**i)
        return sum
    def __deriv__(self):
        new=Polynomial([])
        for i in range(len(self.lis)-1):
            new.lis+=[0]
        for i in range(1,len(self.lis)):
            new.lis[i-1]=i*self.lis[i]
        return new
        

F=Polynomial([2,0,0,0,1])
G=Polynomial([0,1,0,1])
print("F =",F)
print("G =",G)
print("F+G =",F+G)
print("F-G =",F-G)
print("F*G =",F*G)
print("F(2)=",F(2))
print("F' =",F.__deriv__())
