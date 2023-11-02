#askisi 2 Christodoulos
#!/bin/python3
import numpy as np


def simpson(f,a,b,n):
    dx = float(b-a)/(n-1)
    result = 0
    for i in range(0,n-2,2):
        xa = a + i*dx
        xb = a + (i+1)*dx
        xc = a + (i+2)*dx
        result += (f(xa) + 4*f(xb) + f(xc))
    result *= dx/3
    return result

def f(t):
    if t>=1 and t<=5:
        return 2*t
    if t>5 and t<=14:
        return 5*t*t+3
    else:
        return 'error'

print("Simpson's method: %f"%simpson(f,2,9,3))
#   1200.500 (me dio ipodiastimata)

#===========
#   4/4
#===========
