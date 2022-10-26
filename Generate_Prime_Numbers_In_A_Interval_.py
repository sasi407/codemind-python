z=int(input())
m=int(input())
c=0
for k in range(z,m+1):
    for j in range(1,k+1):
        if k%j==0:
            c+=1
    if c==2:
        print(k)
    c=0