a,b,c=map(int,input().split())
p=(a+b+c)*0.5
a=(p*((p-a)*(p-b)*(p-c)))**0.5
print("{:.2f}".format(a))