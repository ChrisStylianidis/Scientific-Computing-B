#!/bin/python3


def greet(msg="Hello",*argv):
    print(msg,end=" ")
    for arg in argv:
        print(arg,end=" ")
    print()
    
name1=input("Give first name:")
name2=input("Give second name:")
greet("Hello",name1,name2,"John","Jane","Jasper")
