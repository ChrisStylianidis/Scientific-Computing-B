#Christodoulos Stylianides Askisi 3 1065882
#!/bin/python3

def rev(a):
    s=""
    for i in range(len(a)-1,-1,-1):
        s+=a[i]
    return s

L=["deer","net","racecar","ten","reed","refer","raw","war","addition","frequency","platform","according","madam"]#pera apo to paradigma prosthesa 2 lekseis pou einai palindromes gia na elegkso oti den tis vlepei to programma

Ans=dict()
for i in range(len(L)):
    for j in range(i+1,len(L)):
    
        if(L[i]==rev(L[j])):
            Ans[L[i]]=L[j]


print(list(Ans.items()))
            
#check ===================
#1) sxolia:         0.5/1    
#2) den trexei:     3/3    
#3) sfalma logikis: 6/6    
#=========================
#Sum                9.5/10
