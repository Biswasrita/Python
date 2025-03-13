n=int(input("Enter the year:"))
if 999<n<10000:
    if n%400==0 and n%100==0 :
        print("It is a leap year")
    elif n%4==0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    print("Invalid Input")                   