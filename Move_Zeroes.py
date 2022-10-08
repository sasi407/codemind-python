n=int(input())
m=list(map(int,input().split()))
a=[]
for i in range(len(m)):
    if m[i]!=0:
        a.append(m[i])
b=len(a)
c=n-b
for k in range(1,c+1):
    a.append(0)
print(*a)