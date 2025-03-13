'''
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
show(5) 
'''
'''
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
f=fact(5)
print(f)
'''
'''
def natural(n):
    if(n==0):
        return 0
    
    return natural(n-1)+n
sum=natural(5)
print(sum)
'''
#write a recursive function to print all elements in a list .
#Hint: use list and index as parameters.
list=["a","b","c"]
