
'''n=int(input("Enter n:"))
#p=65
for i in range(n):
    p=65
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
        p=p+1
    print()
    '''
'''
n=int(input("Enter n:"))
for i in range(n):
    p=65
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
        p=p+1
    print()
'''

'''
n=int(input("Enter n:"))
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    p=p+1
    print()
'''


n=int(input("Enter n:"))
for i in range(1,2*n):
    if i<n:
        print("*"*i)
    if i==n:
        print("*"*(2*n-1))
    if i>n:
        print(" "*(i-1)+"*"*(2*n-i))





