#Christodoulos Stylianides
#!/bin/python3
import numpy as np

a=float(input("Give a: "))
b=float(input("Give b: "))
c=float(input("Give c: "))

p=-(a**2)/3+b
q=(2/27)*(a**3)-(a*b)/3+c
R=(p**3)/27+(q**2)/4
A=np.cbrt(-q/2+np.sqrt(R))
B=np.cbrt(-q/2-np.sqrt(R))
X0=A+B-a/3
print("the solution is:",X0)
exit()
