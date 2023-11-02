#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
from random import randint
myfile=open("SelectedNumbers.dat","w")

def IsSuccessful(a,d=0):
    while(a>0):
        if(a%10==d):
            return True
        a=int(a/10)
    return False

def IsSuccessfulStr(a,d):
    for i in a:
        if i==d:
            return True
    return False

uplim=123456789

digit=input("Give Digit: ")
try:
    digit=int(digit)
except:
    digit=0

myfile.write("Numbers containing the number {:d}\n".format(digit))
for i in range(100):
    x=randint(1,uplim)
    if IsSuccessful(x,digit):
        myfile.write("%d\n"%x)
exit()
    
