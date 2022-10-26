z=int(input())
s=0
p=1
while z!=0:
    r=z%10
    s=s+r
    p=p*r
    z=z//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")