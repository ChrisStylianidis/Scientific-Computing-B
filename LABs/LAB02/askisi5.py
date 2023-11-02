

def fix(a,b,c):
    if a>b and a>c:
        if b>c:
            return a,b,c
        return a,c,b
    if b>a and b>c:
        if a>c:
            return b,a,c
        return b,c,a
    if c>a and c>b:
        if a>b:
            return c,a,b
        return c,b,a



a=int(input("Give a: "))
b=int(input("Give b: "))
c=int(input("Give c: "))



a,b,c=fix(a,b,c)
print(a,b,c)
