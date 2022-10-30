n,m=map(int,input().split())
for i in range(1,m+1):
    if i%2:
        a=n*i
        print(n,"x",i,"=",a)