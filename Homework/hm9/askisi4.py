#Askisi 2 Christodoulos Stylianides 1065882
#!/bin/python3
from random import random,seed
import numpy as np
seed(3141592653)

def printer(area,target):#tipono to map tou fisikoy (8x8)
    print("---------------------------------")#kai stin thesi pou einai
    for rows in area:#tipono ena mavrismeno kouti (den xrisimopoio tin sinartisi) alla itan voithitiki gia tin lisi tis askisis
        for number in rows:
            if(number!=target):
                print("  □",end=" ")
            else:
                print("  ▧",end=" ")
        print()
    print("---------------------------------")

def move(area,target):
    for i in range(len(area)):
        for j in range(len(area)):
            if(area[i][j]==target):
                posi=i
                posj=j#prota vrisko to i kai j tou target
    while(True):
        x=int(4*random())+1
        #i sinartisi doulevei akrivos opws tin askisi 2 
        #moni diafora einai oti den exw midenika stixia ston pinaka
        if(x==1):#boras (panw)
            if(posi>0):
                return area[posi-1][posj]
        elif (x==2):#notos (katw)
            if(posi<7):
                return area[posi+1][posj]
        elif (x==3):#anatoli (deksia)
            if(posj<7):
                return area[posi][posj+1]
        elif (x==4):#disi  (aristera)
            if(posj>0):
                return area[posi][posj-1]
area=np.zeros((8,8))#o xoros pou perpata o fisikos
c=0#arxikopoiisi
for i in range(7,-1,-1):#ksekinaw apo katw -> panw 
    for j in range(8):#aristera -> deksia
        area[i][j]=c
        c+=1

n=50#petiximenes fores pou tha paei
n=int(input("How many times should we torture our physicist? "))
target=63#i thesi deksia panw einai to 63

meter=np.zeros(n)#meter einai o pinakas pou tha vazo to posa vimata
#kanei se kathe taksidi tou mexri na ftasei
for i in range(n):
    meters=0
    target=63
    while(target!=0):#o stoxos einai to 0
        target=move(area,target)
        meters+=1#afksano ta metra kathe fora pou kanw kinisi
    meter[i]=meters#ekso apo to while otan ftasei vazo ta meters sto array
maximum=meter.max()#save ta outs tou programmatos
minimum=meter.min()
average=meter.sum()/len(meter)#mesos oros
for i in range(n):#couts me tin expected (average)
    print("%5d: %5dm, Expected: %5.2fm"%(i+1,meter[i],average))
print("Maximum trip: %7dm"%maximum)
print("Minimum trip: %7dm"%minimum)
print("Average trip: %7.2fm"%average)
printer(area,target)
