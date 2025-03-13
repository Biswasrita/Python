#old_age=input("Enter your old age:")
#(new_age=old_age+2) #can only str (not "int") to str
#print(new_age)
#So the above code is not applicable it throw error
#so to convert it from str to int the following process should be followed--


old_age=input("Enter your old age:")
oa=int(old_age)
new_age=oa +2 #so now it became int
print(new_age)

#from valid value conversion to float,string,boolean--
#float(), str(),  bool()
#example--
number=18
print(float(number))

a=eval(input("Enter:"))
b=eval(input("Enter:"))
sum=a+b
print("The sum of the two numbers:",sum)
