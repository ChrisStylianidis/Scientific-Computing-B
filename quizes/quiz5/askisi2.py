#!/bin/python3
#Christodoulos Stylianides 1065882
class IOclass():
    def __init__(self,st):
        self.st=st
    def passStr(self):
        self.st=input("")
    def printStr(self):
        print((self.st).swapcase())


s=str()
a=IOclass(s)
a.passStr()
a.printStr()
exit()
