z=int(input())
while z:
    if z%2==0:
        z=z//2
    elif z%3==0:
        z=z//3
    elif z%5==0:
        z=z//5
    elif z==1:
        print("Ugly Number")
        break
    else:
        print("Not Ugly Number")
        break