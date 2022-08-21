a=int(input())
x=a%10
y=a//10
while (x+y)>9:
    z=x+y
    x=z%10
    y=z//10
print(x+y)
    