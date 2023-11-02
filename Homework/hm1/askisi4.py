#Christodoulos Stylianides
#!/bin/python3
import numpy as np

def fac(n):
    b=1
    while n>1:
        b*=n
        n-=1
    return b

#x=np.pi/2
x=float(input("Give value of X:"))
given=x
'''
since x is in rads, and since
sinx is periodical, we will reduce it such as
x will be between (0,2pi)
'''
x=x%(2*np.pi)
#past this point, x will be less than 2pi

i=0
y=((-1)**(i))*((x**(2*i+1))/fac(2*i+1))
sum=y
while y>1E-06:
    i+=1
    y=(x**(2*i+1))/(fac(2*i+1))
    if i%2==0:
        sum+=y
    else:
        sum-=y
print("sin({0:.3f})={1:.8f}(The sum given)".format(given,sum))
print("sin({0:.3f})={1:.8f}(Numpy's function)".format(given,np.sin(x)))

exit()
