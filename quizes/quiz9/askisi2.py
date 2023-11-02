#Askisi 2 Christodoulos
#!/bin/python3

from random import random

def check(a,b,c):
    if a==b and a!=c:
        return True
    if a==c and c!=b:
        return True
    if b==c and a!=c:
        return True
    return False

ntries=10000

sum_of_numbers=0
for i in range(ntries):
    a=int(6*random()+1)
    b=int(6*random()+1)
    c=int(6*random()+1)
    if(check(a,b,c)):
        sum_of_numbers+=1

print("Probability:",sum_of_numbers/ntries)
print(5/12)
