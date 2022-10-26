a=int(input())
b=int(input())
c=a+b
d=c+1
i=1
z=0
while True:
    while i<=d:
        if d%i==0:
            z+=1
        i+=1
    if z==2:
        print(d-c)
        break
    d+=1
    z=0
    i=1