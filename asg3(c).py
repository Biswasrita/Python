a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
c=eval(input("Enter c:"))
if a!=0:
    d=b*b-4*a*c
    if d>0:
        r1=(-b+d**0.5)/2*a
        r2=(-b-d**0.5)/2*a
        print(f"The roots are:{r1:.3f},{r2:.3f}")
    elif d==0:
        r=(-b)/2*a
        print(f"The roots are:{r:.3f}")
    else :
        r1=(-b+d**0.5)/2*a
        r2=(-b-d**0.5)/2*a
        print(f"The roots are:{r1:.3f},{r2:.3f}")
else:
    print("Not a quadratic equation")        

            
