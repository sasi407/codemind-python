z=int(input())
s=str(z)
k=[]
for i in s:
    k.append(i)
a=len(k)
p=list(dict.fromkeys(k))
b=len(p)
if a==b:
    print("Unique Number")
else:
    print("Not Unique Number")