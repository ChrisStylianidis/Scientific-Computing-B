#!/bin/python3
#Christodoulos Stylianides 1065882
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
web_file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy145/Exams/data.txt")

dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
def hextodec(number):
    s=0
    for i in range(len(number)):
        try:                       #an einai mono arithmoi tote proxoraei kanonika
            digit=int(number[i])
        except:                    #an exei mesa gramma to kanw arithmo me to dictionary dic
            digit=dic[number[i]]
        s+=digit*16**(len(num)-i-1)#i metafora se dekadiko   #<<< TI EINAI TO NUM???
    return s                                                 #<<< ENNOEIS NUMBER. ETSI OPWS TO EXEIS XALA TO S


def psifia(n):
    return len(n)                  #ta kanw string giati einai poli
                                   #megaloi arithmoi kai den vgenei
num=[]

for n in web_file:
    try:
        num+=[int(n)]              #an den exei gramma
    except:
        n=n.strip()
        n=n.decode('utf-8')  #<<<< AYTO TO XREIAZESAI GIA SWSTI METATROPI XARAKTIRWN
        number=hextodec(n)
        num+=[int(number)]         #vazo toys dekadikoys sto list num

fillme={}                          #dimiourgo adio dictionary
for n in num:
    arithmospsifiwn=psifia(str(n)) #vrisko me tin sinartisi posa digits exei kathe arithmos
    fillme[arithmospsifiwn]=fillme.get(arithmospsifiwn,0)+1
#antistixa se kathe thesi prostheto gia ton kathe arithmo ta antistixa psifia pou exei
a = list(sorted(fillme.items(), key=lambda cnt: (cnt[0], cnt[1])))
#sort ws pros ton arithmo psifiwn dld to key tou dictionary
for digits,freq in a:
    print("%5d-psifiwn arithmoi:%5d"%(digits,freq))#print
x=[]
for i in a:
    x+=[int(i[0])]
y=[]
for i in a:
    y+=[int(i[1])]

plt.xlabel("Number of Digits")
plt.ylabel("Frequency")
plt.title("Askisi3")
plt.grid(True)
plt.plot(x,y,'k--')
plt.plot(x,y,'r.')
plt.savefig("askisi03.pdf")
plt.show()
exit()
#===================
# Apo to grafima fainetai oti kati
# den paei kala me to conversion twn
# arithmwn giati exeis noumera me
# perissotero apo 10000 psifia
#===================
# Sxolia:       3/3
# Compilation:  7/7
# Algorithmos: 13/15
#===================
# Sunolo:      24/25
#===================
