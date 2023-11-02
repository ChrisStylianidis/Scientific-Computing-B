#Christodoulos Stylianides Askisi 2 1065882
#!/bin/python3
import numpy as np

def isit(key,value):
    if key not in s:
        return False
    else:
        if s[key]==value:
            return True
    return False

s=dict()
s["title"]="We are the Champions"
s["albus"]="News of the World"
s["artist"]="Queen"
s["genre"]="Arena rock"
s["release_year"]="1977"
s["length"]="2.59"
s["length_seconds"]="179"
s["songwriter"]="Freddie Mercury"
s["producers"]="Queen, Mike \"Clay\" Stone"

#(a)
print("\n(a):",s)
#(b)
keyss=list(s.keys())
valuess=list(s.values())
print("\n(b)",[(i,s[i]) for i in keyss])

#(c)
klidi=input("\nGive Key to check:\n")
ans=input("Give the value for %s:\n"%(klidi))
print("(c):The information you have provided is: %s"%(isit(klidi,ans)))
exit()
