#Christodoulos Stylianides 1065882
#Askisi 1
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt


def dixot(f,a,b):
    middle=(a+b)/2#ksekino vriskontas tin mesi tou a,b
    if( f(a) > f(b) ):#an einai afksousa i fthinousa (true=fthinousa)
        while(abs(f(middle))>1E-4):#afou theloume akrivia 4 dekadika prepei to f(middle) na einai mikrotero apo to 0.0001 dld na einai poli konta sto 0
            if(f(middle)>0):#an einai thetiko paei na pei oti theloume na kinithoume pio deksia ara to aristero orio plisiazei sto middle
                a=middle
            else:#analoga an einai arnitiko i lisi mas einai sta aristera ara to deksi orio ginete to middle
                b=middle
            middle=(a+b)/2#afou allazoun ta oria mporo na kanw kathe fora a+b/2
    else:
        while(abs(f(middle))>1E-4):#ksana i idia diadikasia gia afksousa
            if(f(middle)>0):
                b=middle#an einai afksousa kai to f einai thetiko thelw 
            else:#na kinithei sto aristero meros ara b=middle
                a=middle#analoga an einai arnitiko sta deksia einai i lisi
            middle=(a+b)/2
    return middle#epistrefo tin lisi me akrivia 4 dekadika


f=lambda x: (x**3-5*x+3)#dimiourgo lambda function gia ton typo tis f

x=np.linspace(0,3,1000)#dio thetikes ara to x einai apo to 0 mexri +apeiro
y=f(x)#dimiourgo 2 arrays
miden=np.zeros(1000)#dimiourgo ena array me midenika gia na 
#sxediaso tin y=0 kai x=0
plt.plot(x,y,'r--',label="f(x)")
plt.plot(x,miden,'k')#x=0
x=np.linspace(0,f(3),1000)#allazo to orio etsi oste
#ston y aksona na ftanei mexri tin timi tou f(3)
plt.plot(miden,x,'k')#y=0
plt.text(0.9,0.70,r'$f(x)=x^3-5x+3$',fontsize=12)#afinw ws text tin f(x)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()#parousiazo ta labels
plt.grid(True)
#i proti lisi einai metaksi tou 0.5 kai 1.0
#i defteri lisi einai metaksi tou 1.5 kai 2.0

x1=(dixot(f,0.5,1.0))
x2=(dixot(f,1.5,2.0))
print("The solutions of the equation f(x):")
print("x1:%.4f\nx2:%.4f"%(x1,x2))

plt.show()


#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10

