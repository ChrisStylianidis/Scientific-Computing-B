#Christodoulos Stylianides
#!/bin/python3


x0=0
v0=1
a=-1.5
dt=0.01

t=0
x=x0
while x>=0:
    print("Object's position: {0:.5f}m at {1:.2f}s".format(x,t))
    t+=dt
    x=x0+v0*t+a*(t**2)/2
print("Time of landing:{:.2f}s".format(t))
#i mathimatiki lisi einai to 4/3 dld 1.3333
#to apotelesma tou provlimatos einai 1.34 afou,
#otan to t=1.33 to x einai akomi thetiko, eno otan
#to t=1.34 tha einai arnitiko ara tha vgei apo to loop
exit()

#check ===================
#1) sxolia:         1/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                10/10
