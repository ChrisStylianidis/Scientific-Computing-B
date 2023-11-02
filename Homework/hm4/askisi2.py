#Christodoulos Stylianides 1065882
#!/bin/python3
def rev(word):
    r=""
    for i in range(len(word)-1,-1,-1):
        r+=word[i]
    return r
def fix(d):
    if(d==10):
        return "A"
    if(d==11):
        return "B"
    if(d==12):
        return "C"
    if(d==13):
        return "D"
    if(d==14):
        return "E"
    if(d==15):
        return "F"
dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}

def hextodec(number):
    s=0
    for i in range(len(number)):
        try:
            digit=int(number[i])
        except:
            digit=dic[number[i]]
        s+=digit*16**(len(num)-i-1)
    return s


def dectodex(number):
    s=""
    while(number>0):
        digit=number%16
        if(digit>9):
            s+="%s"%(fix(digit))
        else:
            s+=str(digit)
        number=int(number/16)
    s=rev(s)
    return s

num=input("Give number in hexadecimal form:")
print("The number (%s) is: %d (decimal)"%(num,hextodec(num)))

dec=int(input("Give number in decimal form:"))
print("The number (%d) is: %s (hexidecimal)"%(dec,dectodex(dec)))

#print("(hex to dec) %d"%int(num,16)) #Python's way of hex to dec
