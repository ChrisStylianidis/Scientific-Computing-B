#Christodoulos Stylianides 1065882
#!/bin/python3
import numpy as np
myfile=open('askisi2.dat','w')

def fac(n):
    b=1
    while n>1:                          #mexri na ginei 1 to n
        b*=n                            #pollaplasiazo sto b 
        n-=1                            #afero ena apo to n gia na ftasei sto 1
    return b                            #epistrefo to factorial

def erf(x):
    s=0
    oros=1
    k=1
    numberoforos=1                      #ksekinao apo ton proto epidi o oros einai 1 otan to k=1
    while abs(oros)>1E-5:               #mexri o oros na einai mikroteros apo 1x10^-5 
        oros=((-1)**k)/((2*k+1)*fac(k))
        oros=x**(2*k)*oros              #ipologizo ton oro me vasi tin ekfonisi
        s+=oros                         #sum ara to prostheto sto s pou arxika itan 0
        numberoforos+=1                 #metrao posous orous ipologizo
        k+=1                            #afksano to k kathe fora
    s=s*(2*x)/(np.sqrt(np.pi))          #pllsiazo me to 2x/riza(pi)
    return s,numberoforos               #epistrefo tin timi kai to N

x=np.arange(0.5,2.25,0.25)              #2.25 gia na parei tin timi tou 2
print(f'{"x        erf(x)     N":^24s}')
print(f'{"="*24}')                      #ta kanw kai sto file kai sto terminal 
myfile.write(f'{"x        erf(x)     N":^24s}\n')
myfile.write(f'{"="*24}\n')             #epikefalida kai diaxoristiki grammi me '='
for i in x:
    erfx,N=erf(i)
    print(f'{i:.2f}\t{erfx:9.5f}{N:>6d}')
    myfile.write(f'{i:.2f}\t{erfx:9.5f}{N:>6d}\n')

'''
tipono to i pou einai stin ousia to x me 2 dekadika 
meta \t kai tipono tin timi tou olokliromatos
kai telos to N to opoio einai o arithmos ton oron pou xriastikan 6 theseis meta to erf(x)
'''
myfile.close()
exit()
