#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np

def sqroot(n):
    L=0#theoro oti i riza tou n
    R=n#einai metaksi tou 0 kai tou n
    while(R-L>1e-15):#oso i diafora twn orion einai megaliteri twn 15 dekadikon
        M=(L+R)/2#vrisko to meso tous
        z=M*M#vrisko ton kivo tou
        if(z<n):#an o kivos tou einai mikroteros apo to 17 (p.x)
            L=M#tote psaxno sto deksi meros giafto L=M
        else:
            R=M#antitheta psaxno sto aristero meros
    return M#epistrefo to M to opoio exei akrivia 15 dekadika

class solutions:
    def __init__(self,f,a,b,eps=1e-4):#tin akrivia tin vazo se periptosi pou
        self.f=f#o xristis den exei sigkekrimeni protimisi
        self.a=a
        self.b=b
        self.eps=eps
        
    def brute(self):
        print("BruteForce method: ",end="")#dixno kathe fora pio method
        #xrisimopoiite
        x=np.linspace(self.a,self.b,1001)
        y=self.f(x)
        root=None
        roots=[]
        for i in range(len(x)-1):#akoloutho tis entoles apo tin dialeksi
            if y[i]*y[i+1]<0:#an iparxei allagi prosimou se dio sinexomena
                root=x[i]-(x[i+1]-x[i])/(y[i+1]-y[i])*y[i]#vrisko lisi
                roots.append(root)#tin vazo stin lista
        if len(roots)==0:#an den vrethoun epistrefo oti den vrethikan
            return "No roots found"
        for i in range(len(roots)-1):
            print("x=%.4f,"%roots[i],end=" ")
        print("x=%.4f"%roots[len(roots)-1],end="")
        return ""#den vazo kati return afou exw idi tipwsei tis liseis

    def newton(self,dfdx):
        print("Newton     method: ",end="")#"title" gia to method
        x=(self.a+self.b)/2#epd den dinete x perno to meso twn orion
        f_value=self.f(x)
        counter=0
        while abs(f_value)>self.eps and counter<100:
            try:
                x-=f_value/dfdx(x)#try giati an einai 0 o paronomastis,
            except:#tha kanw return to error
                return "Cannot divide by 0, x = %.4f"%x
            f_value=self.f(x)
            counter+=1
        if abs(f_value)>self.eps:#afto ginete giati mporei sto counter==100
            counter-=1#na vrethei i lisi abs(f_value)>eps ara afero ena gia na min einai 100 to counter
        if(counter==100):#an einai 100 paei na pei oti den vrethike i lisi
            return "No solution"
        return "x=%.4f, counter=%d"%(x,counter),x

    def secant(self):
        print("Secant     method: ",end="")
        f_x0=self.f(self.a)
        f_x1=self.f(self.b)
        x0=self.a
        x1=self.b#onomazo tis metavlites etsi gia efkolia 
        counter=0#afou kai stin dialeksi etsi einai
        x=1
        while abs(f_x1)>self.eps and counter<100:
            try:
                denominator=(f_x1-f_x0)/(x1-x0)#paronomastis
                x=x1-(f_x1)/denominator#mporei na einai kai edw 0 giafto
            except:#vazo try except
                return "error found denominator zero, x=%.4f"%x
            x0=x1
            x1=x
            f_x0=f_x1
            f_x1=f(x1)#allazo tis aparetites times
            counter+=1
        if abs(f_x1)>self.eps:
            counter-=1#to idio me to newton
        if(counter==100):
            return "No solution"
        return "x=%.4f, counter=%d"%(x,counter)

    def bisection(self):
        print("bisection  method:",end=" ")  
        x_L=self.a
        x_R=self.b
        eps=self.eps
        f=self.f
        f_L=f(x_L)
        x_M=(x_L+x_R)/2.0#x meso
        f_M=f(x_M)#onomasia timwn gia efkolia
        counter=1
        if f_L*f(x_R)>0:
            return "Error! Either even # of solutions or no solution found"
        while abs(f_M)>eps:
            if f_L*f_M>0:#an einai to idio prosimo paw sto deksi meros
                x_L=x_M
                f_L=f_M
            else:#an vrethei lisi paw sto aristero kommati
                x_R=x_M
            x_M=(x_L+x_R)/2#allazo timi tou x_M
            f_M=f(x_M)
            counter+=1
        return "x=%.4f, counter=%d"%(x_M,counter)

        


f=lambda x: 4*np.exp(-2*x)-0.5*x*x#root: 1.01996 (askisi4)
ftonos= lambda x: -8*np.exp(-2*x)-x

g=lambda x: np.exp(-x**2)*np.cos(4*x)
gtonos= lambda x: np.exp(-x**2)*(-2*x*np.cos(4*x)-4*np.sin(4*x))

sq=lambda x: x**2-5*x+6
sqtonos=lambda x: 2*x-5

riza=lambda x: x**2-17
rizatonos=lambda x: 2*x
'''
dimiourgo 4 sinartiseis
1)einai apo tin askisi 4 stin opoia gnorizoume tin lisi
2)einai apo tis simiwseis kai exei perissoteres apo mia liseis
3)einai mia sinartisi me 2 liseis sto diastima pou dinete
4)oi liseis tis einai +riza17 kai -riza17 gia na ipologiso tin riza17
'''


print("\nf(x)=4e^(-2x)-0.5x^2   xe[-3,3]")
tee=solutions(f,-3,3)
print(tee.brute())
print(tee.newton(ftonos)[0])
print(tee.secant())
print(tee.bisection())
        
print("\nf(x)=e^(-x^2)cos(4x)   xe[0,4]")
more=solutions(g,0,4)
print(more.brute())
print(more.newton(gtonos)[0])
print(more.secant())
print(more.bisection())

print("\nf(x)=x^2-5x+6          xe[1,9]")
sqr17=solutions(sq,1,9)
print(sqr17.brute())
print(sqr17.newton(sqtonos)[0])
print(sqr17.secant())
print(sqr17.bisection())

print("\nf(x)=x^2-17            xe[0,17]")
rizaa=solutions(riza,0,17,1e-14)
print(rizaa.brute())
ans=rizaa.newton(rizatonos)#krataw to ans giati
print(ans[0])#thelw to x (ans[1]) na to tiposo katw me tis rizes 17
print(rizaa.secant())
print(rizaa.bisection())

print("\n       √17  = %16.14f"%sqroot(17))
print("Newton √17  = %16.14f"%(ans[1]))
print("np.sqrt(17) = %16.14f"%np.sqrt(17))

'''
i methodos BruteForce parousiazete ws i pio apotelesmatiki se aftes
tis periptoseis, parolafta se merikes periptoseis den vriskei oles tis liseis
opws to trito paradigma(kamia apo tis dio)

i methodos Newtow parousiazete na einai i pio epitixis apo plevras akrivias
(diladi sosti lisi) kai elaxisto arithmo counters
  
'''
#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10
