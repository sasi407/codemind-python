a=int(input())
b=int(input())
s=0
t=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        t+=j
if s==b and a==t:
    print("Amicable")
else:
    print("Not Amicable")