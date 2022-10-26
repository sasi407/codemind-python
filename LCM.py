x,y=map(int,input().split())
s=min(x,y)
b=max(x,y)
i=1
j=1
while True:
    m1=b*i
    while True:
        m2=s*j
        if m1==m2:
            print(m1)
            break
        elif m1<m2:
            break
        else:
            j+=1
            continue
    if m1<m2:
        i+=1
    if m1==m2:
        break