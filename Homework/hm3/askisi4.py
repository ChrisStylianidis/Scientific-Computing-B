#Christodoulos Stylianides Askisi 4 1065882
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

myfile=open("population.txt")
pop=dict()
L=[]
for line in myfile:
    words=line.split()
    L.append(words[len(words)-1])
for i in range(1,10):
    pop[str(i)]=0
for i in L:
    pop[i[0]]+=1
x=list(pop.keys())
y=(list(pop.values()))
for i in range(len(y)):
    y[i]=y[i]/len(L)*100
for i in range(9):
    print("Number {0:s}: {1:3.3f}%".format(x[i],y[i]))


plt.xlabel("Number")
plt.ylabel("Frequency of Appearance (%)")
plt.plot(x,y,'k')
plt.grid(True)
plt.show()
