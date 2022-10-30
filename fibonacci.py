z=int(input())
c=0
a=0
b=1
if z==1:
    print(0)
elif z==2:
    print(1)
else:
    for i in range(1,z+1):
        if i<2:
            print(i-1,end=" ")
            continue
        a=b
        b=c
        c=a+b
        print(c,end=" ")