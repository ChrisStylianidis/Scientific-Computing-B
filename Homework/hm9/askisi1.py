#Askisi 1 Christodoulos Stylianides 1065882
#!/bin/python3
from random import random,seed
import numpy as np
seed(3141592653)

M=int(input("How many balls do you want to take each time? "))#input

while(M<=1 or M>=100):#se periptosi pou dosei lathos arithmo gia mpales
    M=int(input("Please insert a valid number for balls (1<M<100): "))


ntries=int(input("How many attempts each time? "))
box=np.ones(100)
'''
dimiourgo ena pinaka box sto opoio einai oles oi theseis 1
an thelw na afereso mia mpala apo to kouti tha kanw tin thesi tis apo 1 0
'''
p=0#i pithanotita stin opia tha prosthesw tis fores pou tha isxiei i sinthiki
#kai meta tha kanw /ntries
for j in range(ntries):#gia ton arithmo pou dinei o xristis ksekino loop
    box=np.ones(100)#vazo oles tis mpales mesa
    sum=0#arxikopoio to sum
    for i in range(M):
        x=int(random()*100)#dimiourgo ena tixeo x apo to [0,100) , den mporei
        #na einai pote 100 ara apo to 0 mexri kai to 99 einai 100 mpales
        #ara sosta
        while(box[x]==0):#oso to x einai mia mpala i opia exei idi xathei psaxno na vro mia alli mpala pou na einai mesa sto kouti
            x=int(random()*100)
        #vgenontas apo to while to x einai i thesi stin opoia einai sto box 
        #kai orizontas to me box[x]=0 tin vgazo apo to box
        box[x]=0
        sum+=(x+1)#prostheto to x+1 sto sum (giati i mpala me 0 einai i 1) kai i 99 einai i 100
    if(sum>500):
        p+=1
print("The possibility of the sum of {0:d} Balls to be more than 500 is: {1:0.4f}".format(M,p/ntries))
#an epilegoun 32 mpales kai panw einai 100% pithanotita na einai pano apo 500
#32+31+30+29+...2+1>500
#33x16>500 <=> 528>500
exit()
