#!/bin/python3

def y(x):
    return x*x-x

print("x\ty")
print("0.0\t{:.2f}".format(y(0)))
print("1.0\t{:.2f}".format(y(1.0)))
print("2.0\t{:.2f}".format(y(2.0)))
print("3.0\t{:.2f}".format(y(3.0)))

exit()
