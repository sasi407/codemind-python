n=int(input())
m=list(map(int,input().split()))
a=int(input())
f=True
for i in range(len(m)):
    if m[i]==a:
        print(i)
        f=False
        break
if f==True:
    print(-1)