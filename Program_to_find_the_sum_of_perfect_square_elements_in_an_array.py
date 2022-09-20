a=int(input())
b=list(map(int,input().split()))
s=0
a=0
for i in b:
    a=i**0.5
    if a==int(a):
        s+=i
print(s)