def is_prime(n):
    if n==1 or n==0:
        return False
    for m in range(2,n):
        if n%m==0:
            return False
    return True
t=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if is_prime(i)==True:
        b.append(i)
z=float(sum(b)/len(b))
print("{:.2f}".format(z))