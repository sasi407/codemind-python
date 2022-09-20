a= int(input())
z=""
x=[]
b=list(map(int,input().split()))
c=str(b)
for i in b:
    i=str(i)
    z+=i
z=int(z)
z+=1
z=str(z)
for j in z:
    x.append(j)
print(*x)