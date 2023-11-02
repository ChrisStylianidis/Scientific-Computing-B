
N=int(input("Give size of array: "))

summ=0
for i in range(N):
      a=int(input("give the #%d number "%(i+1)))
      summ+=a
print(summ/N)
