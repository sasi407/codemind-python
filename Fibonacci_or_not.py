z=int(input())
a=0
b=1
c=0
arr=[]
arr.append(a)
arr.append(b)
while True:
    if c>z:
        break
    a=b
    b=c
    c=a+b
    arr.append(c)
if z not in arr:
    print(False)
else:
    print(True)