n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=[]
for i in m:
    c=i*i
    a.append(c)
a.sort()
print(*a)