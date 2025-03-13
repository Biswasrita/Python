n=int(input("Enter n:"))
a=0
b=1
c=0
if(n<=0):
    print("Enter positive number")
else:
   print("Fibonacci series:")
   for i in range(1,n+1):
        if n==1:
            print(a)
        else:
            print(a,end=" ")
            c=a+b
            a=b
            b=c