#Christodoulos Stylianides 1065882
#!/bin/python3

import numpy as np

def P(n,x):
    if n<0:
        return 0
    if n==0:
        return 1
    return (2*n-1)*x*P(n-1,x)/n-(n-1)*P(n-2,x)/n


x=np.arange(0,1.1,0.1)
P1=P(1,x)
P2=P(2,x)
P3=P(3,x)
P4=P(4,x)
P5=P(5,x)
myfile=open("hm2_prob4.txt","w")
myfile.write("x         P1:      P2:       P3:       P4:      P5:\n")
print("x         P1:      P2:       P3:       P4:      P5:")
for i in range(len(x)):
    myfile.write("{0:.1f} {1:9.2f} {2:9.3f} {3:9.3f} {4:9.3f} {5:9.4f}\n".format(x[i],P1[i],P2[i],P3[i],P4[i],P5[i]))
    print("{0:.1f} {1:9.2f} {2:9.3f} {3:9.3f} {4:9.3f} {5:9.4f}".format(x[i],P1[i],P2[i],P3[i],P4[i],P5[i]))

#check ===================
#1) sxolia:         0/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                9/10
