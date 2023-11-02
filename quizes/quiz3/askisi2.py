#Christodoulos Stylianides 1065882
#!/bin/python3
#Askisi 2

def sort_list(mylist):
    sort=False
    while(sort==False):
        sort=True
        for i in range(len(mylist)-1):
            if(mylist[i]<mylist[i+1]):
                k=mylist[i+1]
                mylist[i+1]=mylist[i]
                mylist[i]=k
                sort=False
    return mylist
myfile=open("mylist.dat")

for i in myfile:
    x=i.split()
y=[]
for i in range(len(x)):
    x[i]=int(x[i])
    y+=[x[i]]
sorted=sort_list(x)
print("not sorted:\tsorted:")

for i in range(len(x)):
    print("%8d      %6d"%(y[i],sorted[i]))
