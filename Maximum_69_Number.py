z=int(input())
s=str(z)
f=True
k=""
for i in s:
    if int(i)==6 and f==True:
        k=k+"9"
        f=False
    else:
        k=k+i
print(int(k))