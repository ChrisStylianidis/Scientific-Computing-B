#!/bin/python3
lista=[]
myfile=open("lab03_prob1.dat")
for line in myfile:
    x=line.split('\n')
    lista+=[int(x[0])]#to evala int epd eida oti einai ola integer
myfile.close()
print("The list is:")
print(lista)
lista.reverse()
print("The list reversed is:")
print(lista)
exit()
