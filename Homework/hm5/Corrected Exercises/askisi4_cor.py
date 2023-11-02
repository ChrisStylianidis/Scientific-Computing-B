#Christodoulos Stylianides 1065882
#Askisi 4
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

f1=lambda x: 4*np.e**(-2*x) # x**4-1
f2=lambda x: 0.5*x**2 
f=lambda x: 4*np.e**(-2*x) - 0.5*x**2# x**4-1-0.5*x**2
dfdx=lambda x: -8*np.e**(-2*x)-x # 4*x**3-x
'''
oi eksisoseis pou exo se simiosi einai prospathies
gia na do an epistrefei 2 solutions

dimiourgo oles tis aparetites sinartiseis me lambda functions,
f1,f2,f kai i paragogos tis f i opoia tha xrisimopoiithei sthn methodo 
newton
'''

def bisection(f,L,R):
    areas=np.linspace(L,R,100)#dimiourgo ta diastimata apo L sto R 
    ans=[]
    for i in range(99):#mexri to 99 giati to i+1 den mou epitrepei mexri to 100
        a=f(areas[i])#to aristero meros
        b=f(areas[i+1])#to deksi
        if (a*b) < 0:
            #an iparksei allagi prosimou sto a b iparxei kai lisi
            ans.append((areas[i],areas[i+1]))#ta vazo se ena tuple pou tha epistrepso ws lista (ans) sto telos tis function
    if len(ans)==0:
        return bisection(f,L-1,R+1)#simiosi apo kato
    return ans
'''
an den vrethoun liseis tote afksano to orio kai ksana psaxno, o logos pou den to vazo stin arxi afto to if einai epidi mporei i sinartisi na exei 2 liseis ara to prosimo na einai to idio kai sto L kai sto R alla na iparxoun liseis
'''

def newton(f,dfdx,x,eps):#newton raphson
    fx=f(x)
    counter=0
    while(abs(fx)>eps and counter<100):#to counter<100 to vazo giati an me petaksi tha to xaso
        try:#vazo try gia tin periptosi pou i paragogos einai 0
            x=x-fx/dfdx(x)
        except:
            print("Cant divide by 0!")
            return x,counter#epistrefo anti na kanw exit(1)
        fx=f(x)#an ontos i epistrofi einai ektos orion tha elegxtei
        counter+=1#apo to if pou exw stin ektiposi an einai ektos orion
    if abs(fx)>eps:#i to counter na einai megalitero apo to 50
        counter-=1
    return x,counter
            
    
left=float(input("Give lower limit:"))
right=float(input("Give higher limit:"))#input orion (pou mporei na allaktoun)

x=np.linspace(left,right,1000)#to -3 3 dinete apo tin ekfonisi
#an allaktei kai ginei -1 1 i lisi tha einai i idia sta 5 dekadika 

y1=f1(x)
y2=f2(x)
y=y1-y2

plt.plot(x,y1,'k',label="$4e^{-2x}$")
plt.plot(x,y2,'b',label="$0.5x^2$")
plt.plot(x,y,'g',label="$4e^{-2x}-0.5x^2$")#plots and labels
plt.grid(True)
plt.legend(loc="best")#parousiasi tou legend 
diastimata=(bisection(f,left,right))#vrisko ta diastimata
roots=[]
for i in diastimata:
    mesi=(i[0]+i[1])/2#epd to bisection dinei diastima gia kathe newton perno tin mesi timi tou diastimatos pou dinete
    roots.append(newton(f,dfdx,mesi,1e-5))#asko tin newton sta diastimata pou vrika
tipothike=True#arxikopoio tin bool metavliti pou xrisimopoieite pio kato gia tipoma
for i in range(len(roots)):
    if(roots[i][1]>50 or (diastimata[i][0]>roots[i][0]<diastimata[i][1])):#an i lisi einai extos tou diastimatos pou xrisimopoiithikan gia to newton (dld an o algorithmos mas petakse)
        print("The solution was thrown: %8.5f"%roots[i][0])#an to counter tou newton einai panw apo 50 paei na pei oti i lisi den einai sosti
        print("Initial interval: [%.2f,%.2f]"%(left,right))
        tipothike=False#vazo afti tin bool etsi oste an i lisi petaktei na min ksana tiposo ta oria pou dothikan (left,right)
    else:
        print("Solution(s): %8.5f "%(roots[i][0]))#ektiposi
    if  left<roots[i][0]>right and tipothike:#se periptosi pou i lisi einai ektos twn arxikon orion kai an den exoun idi tipothei ta oria, ta tipono
        print("Initial interval: [%.2f,%.2f]"%(left,right))
plt.show()

#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10
