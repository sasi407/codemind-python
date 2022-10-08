n=int(input())
a=[]
for i in range(n):
    a,b=map(int,input().split())
    p=list(map(int,input().split()))[:a]
    q=list(map(int,input().split()))[:b]
    p.extend(q)
    p.sort()
    print(*p)