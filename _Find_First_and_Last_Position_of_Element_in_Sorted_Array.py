n=int(input())
m=list(map(int,input().split()))
a=int(input())
f=True
p=False
q=False
for i in range(len(m)):
    if m[i]==a and f==True:
        b=i
        f=False
        p=True
    if m[i]==a and f==False:
        c=i
        q=True
if p==False:
    b=-1
if q==False:
    c=-1
print(b,c)