#!/bin/python3
import math
class MyVector:
    def __init__(self,x,y,z):
    #constructor
        self.x= x
        self.y= y
        self.z= z
    def __str__(self):
        return "MyVector(%f,%f,%f)"%(self.x,self.y,self.z)
    def __add__(self,other):
        return MyVector(self.x+other.x,self.y+other.y,self.z+other.z)
    def norm(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    def eksgin(self,other):
        return MyVector(self.x*other.x,self.y*other.y,self.z*other.z)
    def poll(self,l):
        return MyVector(l*self.x,l*self.y,l*self.z)
    def dier(self,l):
        return MyVector(self.x/l,self.y/l,self.z/l)


class MyPolarVector(MyVector):
    def __init__(self,r,t,p):
        #constructor
        MyVector.__init__(self,r*math.cos(t)*math.cos(p),r*math.cos(t)*math.sin(p),r*math.sin(t))
    def r(self):
        return self.norm()
    def phi(self):
        return math.atan2(self.y,self.x)
    def theta(self):
        return math.asin(self.z/self.norm())
a=MyVector(3.,1.,0.)
b=MyPolarVector(3.,1.,0.)

print(a+b)
