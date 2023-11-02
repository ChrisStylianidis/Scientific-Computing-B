#Askisi 3 Christodoulos Stylianides
#!/bin/python3
import numpy as np


import urllib.request
file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/LAB06/mydata.txt")#me ton tropo tis dialeksis 9 perno to .txt


p,t,h,u=np.loadtxt(file,usecols=(0,1,2,3),unpack=True,skiprows=2)


lista=np.array(lista)#lista se array
file_to_write=open('lab07_prob3.dat','w')
file_to_write.write("\t{0:.3f}\n\n".format(lista))


for line in myfile:
    x,y=line.split(',')

exit()
