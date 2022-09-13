for i in range(int(input())):
    a,b=map(int,input().split())
    if a>b:
        print("NEW PHONE")
    elif a<b:
        print("REPAIR")
    else:
        print("ANY")