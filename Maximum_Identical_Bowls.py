z=int(input())
y=list(map(int,input().split()))
a=sum(y)
while z:
    if a%z==0:
        print(z)
        break
    z-=1