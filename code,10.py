bs=eval(input("Enter the basis pay of an employee: "))
agp=0.5*bs
print(f"AGP is: {agp:0.2f}")
mb=bs+agp
print(f"Merged Basic is: {mb:0.2f}")
da=0.5*mb
print(f"DA is: {da:0.2f}")
hra=0.15*mb
print(f"HRA is: {hra:0.2f}")
total=mb+da+hra
print(f"Total salary of the employee is: {total:0.2f}")