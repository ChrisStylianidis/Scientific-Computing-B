#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
from sympy import *
'''
theoritiki lisi:
ston proto komvo iparxoun 2 piges kai 3 antistaseis
askw deksiostrofa tin methodo revmaton vroxon
E1=-I1*(R1+R1)+R2*(I1+I2)-E2
3=-I1(4)+4(I1+I2)-6
9=4I2
I2=9/4
gia tin deftero vrogxo
E2=-I2(R2+R1+R1)-E2+I1*R2
12=-8*I2+4*I1
12=-8*(9/4)+4I1
12=-18+4I1
I1=15/2

poli pithano na einai lathos kathos den exw idea an akoloutho ton 
sosto tipo i sosti methodo gia tin epilisi twn dio aftwn vrogxon
'''
I1,I2=symbols('I1 I2')#I1 I2 einai oi agnostoi pou psaxno
E1=3
E2=6
R1=2
R2=4#oi times pou dinontai

print(I2,"=",solve(-I1*(R1+R1)+R2*(I1+I2)-E2-E1)[0])#mporei na lithei i eksisosi
#afou to I1 aplopoiite, ara vrisko tin timi tou I2

i2=float(solve(-I1*(R1+R1)+R2*(I1+I2)-E2-E1)[0])#meta tin vazo stin metavliti i2
print(I1,"=","%.1f"%solve(-E2-i2*(R2+R1+R1)-E2+I1*R2)[0])#i opoia tha xrisimopoiithei edw

## check, to provlima isws ksekinaei apo to gegonos oti den lamvaneis
## ipo4in to oti iparxi kai 3o revma, to I3, epomenws thes 3 eksiswseis gia 3 agnwstus
## prospathise na to ksanakaneis, des kai tin lisi kai an exis apories to
## sizitame

#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 4.5/6    
#=========================
#Sum                8.5/10
