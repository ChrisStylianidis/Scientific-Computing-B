#Christodoulos Stylianides 1065882
#!/bin/python3

def f(x):
    oros=0.6
    sum=oros
    i=1
    while(oros>1E-6):
        if(i%2==0):
            oros=1/((2*i-1)*(x**(2*i-1)))
            sum+=oros
        else:
            oros=1/((2*i-1)*(x**(2*i-1)))
            sum-=oros
        i+=1
    return sum

myfile=open('Seira.txt','w')
x=1
while(x<=3.0):
    myfile.write("x={:4.2f}  f(x)={:8.5f}\n".format(x,f(x)))
    x+=0.5
exit()
