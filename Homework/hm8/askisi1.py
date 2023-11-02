#Askisi 1 Christodoulos Stylianides
#!/bin/python3
import numpy as np
from random import random,seed
seed(314159265358979323846264338327950288419716939937510582097494459)
'''
Anagnorizo oti to trigono einai isoskeles kai giafto tha einai efkoli i 
evresi tis eksisosis tou tipou y=|x| me kapies metavlites
i eksisosi einai y=-3|x|+3
kai tha xrisimopoiiso tin methodo montecarlo gia 
x -1,1
y  0,3
profanos afou vasi epi ipsos /2 einai 3 to apotelesma
prepei na einai konta sto 3
'''
f=lambda x: -3*abs(x)+3

def montecarlo(xmin,xmax,ymin,ymax,f,ntries):# i methodos tou monte carlo
    below=0#tis aporripsis, arxikopoio to below
    for i in range(ntries):
        x=(xmax-xmin)*random()+xmin#ta oria tou x
        y=(ymax-ymin)*random()+ymin#kai tou y
        if y<f(x):#an to tixeo y pou epilektike einai katw apo tin f(x)
            below+=1#opou x einai tixeo tote afksanoume to below
    emvado=(xmax-xmin)*(ymax-ymin)#to emvado tou paralilogramou sto opoio psaxnoume
    return emvado*below/ntries#to emvado epi to klasma gia to posa simia efthasan kato apo tin sinartisi einai to olokliroma tis sinartisis aftis
print("A(-1,0) B(1,0) C(0,3)")#ta simia tou trigonou
print("The area of the Triangle is: %.3f"%montecarlo(-1,1,0,3,f,1000000))
