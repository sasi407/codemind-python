z=int(input())
i=0
j=1
while i*j<=z:
    if z==i*j:
        print("YES")
        break
    i+=1
    j+=1
if z!=i*j:
    print("NO")