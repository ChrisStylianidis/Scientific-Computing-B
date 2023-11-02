#Askisi 3 Christodoulos Stylianides 1065882
#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def Nx(y):
    return -wx*y

def Ny(y):
    return -wy*y+wx*Nx(t)

def montecarlo(xmin,xmax,ymin,ymax,f,ntries):# i methodos tou monte carlo
    below=0#tis aporripsis, arxikopoio to below
    for i in range(ntries):
        x=(xmax-xmin)*random()+xmin#ta oria tou x
        y=(ymax-ymin)*random()+ymin#kai tou y
        if y<f(x):#an to tixeo y pou epilektike einai katw apo tin f(x)
            below+=1#opou x einai tixeo tote afksanoume to below
    emvado=(xmax-xmin)*(ymax-ymin)#to emvado tou paralilogramou
    return emvado*below/ntries

Nx0=1000
Ny0=0

wx=0.01
wy=0.002

## check, ??? giati imiteles?
#check ===================
#1) sxolia:         1/1    
#2) den trexei:     1/3    
#3) sfalma logikis: 2/6    
#=========================
#Sum                4/10
