z=int(input())
a=0
b=1
i=0
while True:
    a=b
    c=2**i
    b=c
    if c>=z:
        break
    i+=1
s=abs(a-z)
p=abs(b-z)
print(min(s,p))