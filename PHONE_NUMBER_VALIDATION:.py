a=int(input())
a=str(a)
a=list(a)
if a[0]==0:
    print("Invalid")
else:
    if len(a)==10:
        print("Valid")
    else:
        print("Invalid")