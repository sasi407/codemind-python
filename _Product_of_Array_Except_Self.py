n=int(input())
m=list(map(int,input().split()))
s=1
for i in range(len(m)):
    for j in range(len(m)):
        if i==j:
            continue
        s=s*m[j]
    print(s,end=' ')
    s=1