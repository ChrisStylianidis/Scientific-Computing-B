#Askisi 1 Christodoulos 1065882
#!/bin/python3

def Trapezoid(f,a,b,n):
    dx = (b-a)/float(n)
    s=0.5*(f(a)+f(b))
    for i in range(1,n):
        s = s + f(a + i*dx)
    return dx*s
def f(t):
    if t>=1 and t<=5:
        return 2*t
    if t>5 and t<=14:
        return 5*t*t+3
    else:
        return 'error'

print("Trapezium Rule: %f"%Trapezoid(f,2,9,2))
#   1260.875 (me dio ipodiastimata)


#========
# 4/4
#========
