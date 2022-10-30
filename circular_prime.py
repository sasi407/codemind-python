z=int(input())
m=str(z)
a=m[::-1]
b=int(a)
c=0
d=0
for i in range(1,z+1):
    if z%i==0:
        c+=1
if c==2:
    for j in range(1,b+1):
        if b%j ==0:
            d+=1
    if d==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")