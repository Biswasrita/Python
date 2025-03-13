#Write a program that accepts sets of three numbers, and prints the secondmaximum number among the three.

n=(input("Enter numbers separated by space:"))
integers= [int(i) for i in n.split()]
#print(integers)
if len(integers)==3:
    integers.sort()
    print(integers)
    print("Second largest:",integers[1])
else:
    print("Invalid")