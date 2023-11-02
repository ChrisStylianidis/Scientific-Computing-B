#Askisi 7
#!/bin/python3
import numpy as np
import sympy

def midpoint_double1(f,a,b,c,d,nx,ny):
    hx = (b-a)/float(nx)
    hy = (d-c)/float(ny)
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + hx/2 + i*hx
            yj = c + hy/2 + j*hy
            I += hx*hy*f(xi,yj)
    return I

def f(x,y):#x[-2,5]  y[0,4]
    return 5*x+8*y
a=-2
b=5 #x

c=0
d=4 #y

x,y = sympy.symbols('x y')
I_expected = sympy.integrate(f(x,y),(x,a,b),(y,c,d))
print("Expected Value:    %d"%I_expected)
for nx,ny in (3,5),(4,4),(5,3):
    I_computed1 = midpoint_double1(f, a, b, c, d, nx, ny)

print("Computed Value:    %d"%I_computed1)
