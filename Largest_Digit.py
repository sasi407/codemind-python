a=int(input())
l=[]
while a>0:
    r=a%10
    l.append(r)
    a=a//10
print(max(l))