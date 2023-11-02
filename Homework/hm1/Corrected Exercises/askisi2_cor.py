#Christodoulos Stylianides
#!/bin/python3

import numpy as np

x=np.arange(0,2*np.pi+np.pi/500,np.pi/500)
print("x          sin(x)     cos(x)")
for i in (x):
    print("{0:.5f} {1:10.5f} {2:10.5f}".format(i,np.sin(i),np.cos(i)))
exit()


'''
#(afto to part einai se periptosi pou i askisi zita tous tipous aftous
#se mia lista, i opoia einai disdiastati me 3 stiles)

x=np.arange(0,2*np.pi+np.pi/500,np.pi/500)
lista=np.zeros((len(x),3))
sin=np.sin(x)
cos=np.cos(x)
for i in range(len(x)):
    lista[i,0]=x[i]
    lista[i,1]=cos[i]
    lista[i,2]=sin[i]
print("   x\t\t   sin(x)\t   cos(x)")
print(lista)
exit()
'''

#check ===================
#1) sxolia:         0.5/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                9.5/10
