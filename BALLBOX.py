for i in range(int(input())):
    n,k=map(int,input().split())
    k=(k*(k+1))/2
    if n>=k:
        print("YES")
    else:
        print("NO")
        