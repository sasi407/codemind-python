a=int(input())
#for i in range(a):
for j in range(a,0,-1):
    for k in range(j):
        print(chr(j+64),end=" ")
    print("")