#Askisi 2 Christodoulos Stylianides 1065882
#!/bin/python3
from random import random,seed
import numpy as np
seed(3141592653)

def printer(area,target):#i sinartisi afti tiponei ton xoro
    print("----------------")#kai ena kouti stin thesi pou vriskete
    for rows in area:#o zalismenos simfititis mas :)
        for number in rows:
            if(number!=0 and number!=target):
                print("%3d"%number,end=" ")
            elif (number==target):
                print("  ▧",end=" ")#stin thesi pou vriskete tipono kouti
            else:
                print("   ",end=" ")#keno an einai 0 (4 gonies)
        print()
    print("----------------")#diaxoristika
'''
i sinartisi move stin opoia kinite epistrefontas to target
einai geniki, diladi se periptosi pou vrethei stin thesi 1
mporei na paei deksia sto 2 eno stin askisi afti den dikaioute
afto to "lathos" to ftiaxno pio katw stin main

stin sinartisi dimiourgo ena while, o logos pou einai while kai
den einai xoris while (afou to x tha einai metaksi 1 kai 4)
einai epidi mporei to x na me metaferei se mia apagorevmeni thesi 
sto area, kai giafto exw while, se periptosi pou to x einai lathos
tha ksana mpei sto while loop kai tha allaksei timi tou x

'''
def move(area,target):
    for i in range(len(area)):
        for j in range(len(area)):
            if(area[i][j]==target):
                posi=i
                posj=j#prota vrisko to i kai j tou target
    while(True):
        x=int(4*random())+1
        #gia na paw pros ta panw simenei oti mionete ena apo to rows
        #kai to orio einai pros ta panw ara <0
        if(x==1):#boras (panw)
            if(not(posi-1<0 and area[posi-1][posj]==0)):
                return area[posi-1][posj]
        #gia na pigeno pros ta katw simenei oti afksanete ena sto rows
        #kai afou to katotato simio exei rows=3 an 3+1 < 4 thelw na einai false
        elif (x==2):#notos (katw)
            if(not(posi+1<4 and area[posi+1][posj]==0)):
                return area[posi+1][posj]
        #ta antistixa gia aristera deksia
        elif (x==3):#anatoli (deksia)
            if(not(posj+1<4 and area[posi][posj+1]==0)):
                return area[posi][posj+1]
        elif (x==4):#disi  (aristera)
            if(not(posj-1<0 and area[posi][posj-1]==0)):
                return area[posi][posj-1]
def out(num):#i sinartisi afti empistrefei bool
    if(num>0 and num<4):#an einai sta oria tou area
        return True
    elif (num>5 and num<8):
        return True
    elif (num>9 and num<=12):
        return True
    return False
'''
alli methodos pou tha mporousa na xrisimopoiiso einai 
an eixa to area ws pinaka na elegxo to i j tou target
kai na lew an einai ena apo ta dio iso me 0 i 3 (sta oria)
'''
ntries=int(input("How many times should we torture this student? "))#ntries
area=[[0,1,2,0],[3,4,5,6],[7,8,9,10],[0,11,12,0]]#to area mas

timeshewenttodrink=0#arxikopoiisi counter
for i in range(ntries):#gia toses fores ksekino to for mou
    target=4#ksekinao apo to 4 (ΣΘΕΕ02) kathe fora
    while(target!=10 and target!=11):
        #vgeno apo afto to loop mono an pao se bar i eimai se eksoteriko simio
        target=move(area,target)
        if(out(target)):
            break
    if(target==10 or target==11):#an piga se bar
        timeshewenttodrink+=1#afksano
        #printer(area,target)#tipono kai to area sto opoio vrisketai
print("Posibility of the student reaching the bar: ")#couts ta posibilities
print("%d/%d"%(timeshewenttodrink,ntries))
print("{0:.2f}%".format(timeshewenttodrink/ntries*100))
