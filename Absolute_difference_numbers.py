x,y=map(int,input().split())
s=str(x)
k=len(s)
a=s[:y]
b=s[k-y:k]
z=abs(int(a)-int(b))
print(z)