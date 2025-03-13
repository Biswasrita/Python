n=int(input("Enter rows or size:"))
#print(" *"*5)
'''
for i in range(n):#rows starts with 0
    for j in range(n):#columns
        print("*",end=" ")
    print()
'''
'''
for i in range(n):#rows starts with 0
    for j in range(i+1):#columns
        print("*",end=" ")
    print()
'''
'''
for i in range(n):#rows starts with 0
    for j in range(i,n):#columns
        print("*",end=" ")
    print()
'''
'''
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
'''
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
'''
'''
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")

    print()
'''
'''
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
        
    print()
'''
'''
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
'''
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    print()
#print("*")
for i in range(n):
    
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    #for j in range(i+1):
        #print(" ",end=" ")
    print()

