a=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i<0:
        s.append(len(str(i*-1)))
    else:
        s.append(len(str(i)))
for i in s:
    print(i,end=' ')