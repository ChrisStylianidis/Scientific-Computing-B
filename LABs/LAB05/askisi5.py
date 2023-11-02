#!/bin/python3
import numpy as np

class MyComplex:
    def __init__(self,a=0,b=0):
        #constructor
        self.a= a
        self.b= b
    def __str__(self):
        if self.b<0:
            return "%f - %fj"%(self.a,-self.b)
        return "%f + %fj"%(self.a,self.b)
    def __add__(self,other):
        return MyComplex(self.a+other.a,self.b+other.b)
    def __sub__(self,other):
        return MyComplex(self.a-other.a,self.b-other.b)
    def __mul__(self,other):
        return MyComplex(self.a*other.a-self.b*other.b,self.b*other.a+self.a*other.b)
    def norm(self):
        return np.sqrt(self.a**2+self.b**2)
    def div(self,other):
        Ans=self*MyComplex(other.a,-other.b)
        Ans.a/=(other.norm()**2)
        Ans.b/=(other.norm()**2)
        return Ans
A=MyComplex(5,9)
B=MyComplex(1,2)
print("A+B=",A+B)
print("A-B=",A-B)
print("A*B=",A*B)
print("A/B=",A.div(B))
print("Metro A=",A.norm())
print("Metro B=",B.norm())

