a=eval(input("Enter a : "))
b=eval(input("Enter b : "))
c=eval(input("Enter c : "))
max=a if a>c else c if a>b else b if b>c else c
print("The Greatest Number :",max)