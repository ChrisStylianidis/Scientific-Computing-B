#Christodoulos Stylianides askisi 3
#!/bin/python3
from random import random
import numpy as np
import matplotlib.pyplot as plt
times=1000000
E=0# epitixies
for i in range(times):
    x=-1+2*random()
    y=-1+2*random()
    if (x**2+y**2<=1):
        E+=1
mypi=4*E/times
print("My pi:",mypi)
print("Pi: 3.141593")
exit()
