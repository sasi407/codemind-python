n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=list(map(int,input().strip().split()))[:n]
for i in range(n):
    print(a[i]+b[i],end=' ')
    