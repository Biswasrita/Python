'''
n=input("Enter statement:")
l=n.swapcase()
print(l)
'''
'''
n=input("Enter email:")
l=n.split("@")
print("The college roll no and the institute name:"+ l[0],end=" ")
l1=l[1].split(".")
print(l1[0].upper())
'''
'''

n=eval(input("Enter an integer:"))
if 1<=n<=100:
    if n%2!=0:
        print("Weird")
    if n%2==0:
        for i in range (2,6):
            print("Not Weird")
        for i in range (6,21):
            print("Weird")
        if i>20:
            print("Not Weird")
else:
    print("Invalid Input")            
                '''
'''
n=int(input())
if 1<=n<=100:
    if n%2!=0:
        print("Weird")
    if n%2==0:
        for i in range (2,6):
            print("Not Weird")
        for i in range (6,21):
            print("Weird")
        if i>20:
            print("Not Weird")
else:
    print("Invalid Input")            
   '''
'''
a = int(input())
b = int(input())
print(int(a/b))
print(float(a/b))             
   '''
'''
n = int(input())
if 1<=n<=20:
    for i in range(0,n+1):
        print(i**2) 
'''

def is_leap(year):
    leap = True
    
    return(year%400==0 and year%100==0) or (year%4==0)

year = int(input())
print(is_leap(year))
