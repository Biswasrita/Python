n=int(input("Enter number:"))

sum=0
order=len(str(n))
i=n
while(n>0):
    d=n%10
    sum=sum+(d**order)
    n=n//10
if(sum==i):
    print("The number is armstrong")
else:
    print("Not armstrong")
