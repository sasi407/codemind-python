n=int(input())
m=list(map(int,input().split()))
for i in range(1,n+2):
    if i not in m:
        print(i)
        break