a=int(input())
p=1
s=0
r=0
while a>0:
    r=a%10
    p*=r
    s+=r
    a=a//10
print(p-s)