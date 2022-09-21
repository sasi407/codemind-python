a=int(input())
b=0
for i in str(a):
    if int(i)%2==0:
        b+=1
if b==0:
    print("Odd")
elif b==len(str(a)):
    print("Even")
else:
    print("Mixed")
    