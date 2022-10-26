z=int(input())
s=0
while True:
    r=z%10
    s=s+(r**2)
    z=z//10
    if z==0 and s>9:
        z=s
        s=0
    if z==0 and s<10:
        break
if s==1 or s==7:
    print("True")
else:
    print("False")