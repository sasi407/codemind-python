z=int(input())
f=True
c=0
i=1
r=z
while True:
    k=r
    while i<=k:
            if k%i==0:
                c+=1
            i+=1
    if c==2:
        r=z%10
        if z==0:
            break
        z=z//10
    else:
        print("Not Mega Prime")
        f=False
        break
    i=1
    c=0
if f==True:
    print("Mega Prime")