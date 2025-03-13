#a,b,c=4,5,6

weight=eval(input("Enter weight:"))
height=eval(input("Enter height: "))
bmi=(weight/height**2)
print(f"BMI of the person:{bmi:0.3f}")