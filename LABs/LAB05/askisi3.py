#!/bin/python3


def mt(*argv):
    b=0
    for arg in argv:
        b+=int(arg)
    return b/len(argv)

print(mt("1","2","3","4","5","6"))
