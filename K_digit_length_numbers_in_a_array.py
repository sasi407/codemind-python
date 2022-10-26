a,b=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in l:
    if i<0:
        if len(str(i*-1))==b:
            s+=1
    else:
        if len(str(i))==b:
            s+=1
print(s)