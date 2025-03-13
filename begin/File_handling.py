'''
n=int(input("Enter number:"))
f1=open("Prime.txt","w")
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
ch=0
while(n):
    if is_prime(ch):
        f1.write(str(ch))
        f1.write(" ")
        n=n-1
    ch=ch+1
'''
n=int(input("Enter number:"))
f1=open("Fibonacci.txt","w")
a=0
b=1
while(a<n):
    f1.write(str(a)+"\n")
    a,b=b,a+b
f1.close()
