n=input("Enter a statement:")
a=0
b=0
for i in n:
    if i.isupper():
        a=a+1
    else:
        b=b+1
print(a,end=" ")
print(b)            