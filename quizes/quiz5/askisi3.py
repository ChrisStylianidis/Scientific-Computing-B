#!/bin/python3
class Student():
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def presentation(self):
        print("Hi! To onoma mou einai:",self.name)
    def __str__(self):
        return "Name: %s\nAge: %s"%(self.name,self.age)
class PhDStudent(Student):
    def __init__(self,thesis):
        self.thesis=thesis
    def get_thesis_title(self):
        return "%s"%(self.thesis)
