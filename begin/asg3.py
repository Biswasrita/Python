#max number
'''
a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
c=eval(input("Enter c:"))
max= a if a>c else c if a>b else b if b>c else c
print("The maximum number:",max)
'''

#check leap year or not
'''
n=int(input("Enter year:"))
if 999<n<10000:
    if n%400==0 or n%100==0:
        print("It is leap year")
    elif n%4==0:
        print("It is leap year")
    else:
        print("Not leap year")
else:
    print("Invalid choice")
'''

#Quadratic eq
'''
a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
c=eval(input("Enter c:"))
if a!=0:
    d=b**2-4*a*c
    if d>0:
        r1=(-b+d**0.5)/2*a
        r2=(-b-d**0.5)/2*a
        print(f"The roots are:{r1:.3f},{r2:.3f}")
    elif d==0:
        r=(-b)/2*a
        print(f"The root are:{r:.3f}")
    else:
        r1=(-b+d**0.5)/2*a
        r2=(-b-d**0.5)/2*a
        print(f"The roots are:{r1:.3f},{r2:.3f}")
else:
    print("Not a quadratic")
'''
#vowel consonant
n=input("Enter a character:")
match n:
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("It is vowel")
    case _ if len(n)==1 and n.isalpha():
        print("It is consonant")
    case _:
        print("Wrong input")
