n=int(input())
s=0
a=[]
for i in range(1,n+1):
    m=int(input())
    a.append(m)
t=int(input())
for k in range(len(a)):
    if a[k]<=t:
        s=s+1
    else:s=s+2
print(s)