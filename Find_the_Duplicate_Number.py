n=int(input())
m=list(map(int,input().split()))
a=[]
for i in m:
    if i not in a:
        a.append(i)
    else:
        print(i)
        break