for i in range(int(input())):
    s=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if j%10==2 or j%10==3 or j%10==9:
            s+=1
    print(s)