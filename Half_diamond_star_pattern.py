a=int(input())
i=1
if a>=3:
    a-=1
    while i<=a:
        print(i*"*")
        i+=1 
    a=1
    while i>=a:
        print(i*"*")
        i-=1
else:
    print("The pattern is not possible")