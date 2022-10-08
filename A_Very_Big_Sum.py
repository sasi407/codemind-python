n=int(input())
m=list(map(int,input().strip().split()))[:n]
s=0
for i in range(len(m)):
    s=s+m[i]
print(s)