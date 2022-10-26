z=int(input())
a=z
if z<0:
    z=z*(-1)
s=str(z)
p=""
k=[]
j=0
for i in s:
    k.append(i)
m=k[::-1]
for j in m:
    p=p+j
if a<0:
    b=int(p)
    print(b*(-1))
else:
    print(int(p))