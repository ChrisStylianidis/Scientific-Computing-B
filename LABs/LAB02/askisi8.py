
def fac(n):
    b=1
    while(n>1):
        b*=n
        n-=1
    return b

a=int(input("Give number: "))
print(fac(a))
