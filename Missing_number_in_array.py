for i in range(int(input())):
    n=int(input())
    b=list(map(int,input().split()))
    x=(n*(n+1))//2-sum(b)
    print(x)