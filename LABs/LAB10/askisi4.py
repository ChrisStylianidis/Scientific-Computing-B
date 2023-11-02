#Askisi 4
#!/usr/bin/python3

import numpy as np
from random import seed, random

def func1(x):
    return x**2 * np.exp(-x)

def func2(x,y):
    return y - x - 2*x**2 - 2*x*y - y**2

def find_max1(myfunc1, xlims, mctries):
    fmax  = -9.0E9
    for itry in range(mctries):
        x = xlims.min() + (xlims.max() - xlims.min())*random()
        y = myfunc1(x)
        if y >= fmax:
            fmax = y
            xmn = x
    return xmn, fmax

def find_max(myfunc2, xlims, ylims, mctries):
    fmax = -9.0E9
    for itry in range(mctries):
        x = xlims.min() + (xlims.max() - xlims.min())*random()
        y = ylims.min() + (ylims.max() - ylims.min())*random()
        z = myfunc2(x,y)
        if z >= fmax: 
            fmax = z
            xmx = x
            ymx = y
    return xmx, ymx, fmax

#... Main
seed(123456)
#... Elaxisto
xvals=np.array([0.0, 4.0])
fmin = 9.0E9	# Mia polu megali arxika timi gia to minimum
#... Megisto
fmax = -9.0E9   # Mia poly mikri arxika timi gia to megisto
xlims=np.array([-2.0,2.0])
ylims=np.array([ 1.0,3.0])

icases = 6
print('\n %10s  %20s  %30s' % ('MC tries','Maximum of func1','Maximum of func2'))
print('%20s  %11s  %12s  %10s  %14s' % ('xmax', 'f(xmax)', 'xmax', 'ymax', 'f(xmax,ymax)')) 
for itries in range(icases):
    ntries = 10**itries
    xmax, max_func1 = find_max1(func1,xvals,ntries)
    xmax, ymax, max_func2 = find_max(func2,xlims,ylims,ntries)
    print('{0:7d} {1:14.6f} {2:10.8f} {3:15.8f} {4:11.8f} {5:11.8f}'.
          format(ntries,xmax,max_func1,xmax,ymax,max_func2))

