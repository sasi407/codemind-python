n=int(input())
m=list(map(int,input().split()))
c=0
s=0
for i in m:
    if i==1:
        c+=1
        
    if c>s:
        s=c
    if i!=1:
        c=0
print(s)