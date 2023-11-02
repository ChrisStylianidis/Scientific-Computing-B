#Christodoulos 1065882
#!/bin/python3
import numpy as np

def fac(n):
    b=1
    while(n>1):
        b*=n
        n-=1
    return b
def P(n,a):
    return (a**n)*np.exp(-a)/fac(n)

a=int(input("Give value for a: "))
for i in range(1,21):
    print("for n=%2d the probability is %2.5f"%(i,P(i,a)))
exit()
