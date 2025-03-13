a=input("Enter string:")
b=input("Enter range:")
s=b.split()
q=int((s[0])-1)
r=int(s[1])
x=s[q:r]
y=x[::-1]
print(x)
print(y)
if x==y:
    print("Pallindrome")
else:
    print("Not Pallindrome")
