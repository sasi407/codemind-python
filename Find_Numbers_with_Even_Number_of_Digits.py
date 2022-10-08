n=int(input())
m=list(map(int,input().strip().split()))[:n]
c=0
for i in range(len(m)):
    b=str(m[i])
    a=len(b)
    if a%2==0:
        c+=1
print(c)