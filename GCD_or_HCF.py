a,b=map(int,input().split())
z=min(a,b)
m=max(a,b)
i=1
c=0
while i<=z:
    if m%i==0 and z%i==0:
        if i>c:
            c=i
    i+=1
print(c)