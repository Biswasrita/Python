'''
n=int(input("Enter height:"))
if n>3:
    print("Token required")
else:
    print("not required token")
'''
'''
n=int(input("Enter number:"))
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")
'''
'''
h=int(input("Enter height:"))
if h>=3:
    print("can ride")
    age=int(input("Enter age:"))
    if age<=18:
        print("Pay 200")
    else:
        print("Pay 500")
else:
    print("can't ride")
'''
'''
n=int(input("Enter year:"))
if n%4==0:
    print("This is leap year")
    if n%100==0:
        print("This is leao year")
        if n%400==0:
            print("This is leap year")
        else:
            print("This is not leap year")
    else:
        print("This is not leap year")
else:
    print("This is not leap year")
'''
'''
height=int(input("Enter height:"))
bill=0
if height>=3:
    print("Can ride")
    age=int(input("Enter age:"))
    if age<12:
        bill=150
        print("Ticket price 150 RS")
    elif age<=18:
        bill=250
        print("Ticket Price 250 RS")
    else:
        bill=500
        print("Ticket Price 500 RS")
    want_photo=input("Do you want to take photo?(Y/N?)")
    if want_photo=='Y' or  want_photo=='y':
        bill=bill+50
    print(f"Your total bill is :{bill}")


else:
    print("Can't ride")
'''

'''
m=input("1.Small Size Pizza \n2.Medium Size Pizza \n3.Large Size Pizza")
n=int(input("Enter choice:"))
bill=0
if n==1:
    bill=100
    print("Pizza price 100")
    want_peppperoni=input("Want pepperoni(Y/N)?")
    if want_peppperoni=='Y' or want_peppperoni=='y':
        bill=bill+30
    
elif n==2:
    bill=200
    print("Pizza price 200")
    want_peppperoni=input("Want pepperoni(Y/N)?")
    if want_peppperoni=='Y' or want_peppperoni=='y':
        bill=bill+50
elif n==3:
    bill=300
    print("Pizza price 300")
    want_peppperoni=input("Want pepperoni(Y/N)?")
    if want_peppperoni=='Y' or want_peppperoni=='y':
        bill=bill+50
else:
    print("Wrong choice")
extra_cheese=input("Want extra chesse?(Y/N)")
if extra_cheese=='y' or extra_cheese=='Y':
    bill=bill+20
print(f"Your total bill:{bill}")
'''
'''
name1=input("Enter your name:")
name2=input("Enter his/her name:")
combine_string= name1 + name2
lower_case=combine_string.lower()
t= lower_case.count('t')
r= lower_case.count('r')
u= lower_case.count('u')
e= lower_case.count('e')
true=t+r+u+e
l= lower_case.count('l')
o= lower_case.count('o')
v= lower_case.count('v')
e= lower_case.count('e')
love=l+o+v+e
Total=str(true)+str(love)
print(f"Love Score is :{Total}")
'''



