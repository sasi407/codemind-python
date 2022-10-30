z=int(input())
k=1
p=0
b=0
while True:
    j=str(k)
    m=int(j[::-1])
    if k==m:
        if k==z:
            k+=1
            continue
        b=p
        p=k
    if p>z:
        break
    k+=1
s1=abs(b-z)
s2=abs(z-p)
if s1==s2:
    print(b,p)
elif s1<s2:
    print(b)
else:
    print(p)