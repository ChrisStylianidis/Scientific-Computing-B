#askisi7

a=int(input("Give a: "))
b=int(input("Give b: "))
sum=0
while(b<a):
    print("Wrong Values try again:")
    a=int(input("Give a: "))
    b=int(input("Give b: "))

for i in range(a+1,b,1):
    sum+=i
print("(%d,%d)"%(a,b))
c=b-a-1
print("there are %d numbers"%c)
mo=sum/(c)
print("the sum of those numbers is %d and its average is %f"%(sum,mo))
