def prime(p,k):
    if p>=k:
        if p==0 or p==1:
            return 0
        for i in range(2,p):
            if p%i==0:
                return 0
        return 1
x=int(input())
a=list(map(int,input().split()))
d=int(input())
x=0
for i in a:
    if prime(i,d)==1:
        x+=1
print(x)
    
        