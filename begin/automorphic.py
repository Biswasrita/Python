n=int(input("Enter number:"))
f=0
i=n
t=10
square=n**2
while(n>0):
    r=square%t
    if(r==i):
        f=1
        break
    n=n//10
    t=t*10
if f==1:
    print("The automorphic number ")
else:
    print("Not automorphic")
