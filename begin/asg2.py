#swapping without third variable----
'''
a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
print(f"Before swapping a:{a} and b:{b}")
a,b=b,a
print(f"After swapping a:{a} and b:{b}")
'''

#swapping with third variable
'''
a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
print(f"Before swapping a:{a} and b:{b}")
temp=a
a=b
b=temp
print(f"After swapping a:{a} and b:{b}")
'''

bs=eval(input("Enter Basic Pay:"))
AGP=0.5*bs
mb=bs+AGP
da=0.5*mb
hra=0.15*mb
total=mb+da+hra
print(f"Total salary:{total:0.2f}")