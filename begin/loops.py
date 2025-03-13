'''
#print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1
print("Loop ended")
'''
'''
#print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i=i-1
print("Loop ended")

'''
'''
#print the multiplication table of n number
n=int(input("Enter n:"))
i=1
while i<=10:
    print(n*i)
    i=i+1
'''
'''
#print the elements: 
i=1
l=[]
while i<=10:
    l.append(i**2)
    i=i+1
print (l)
'''
'''
l=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(l):
    print(l[i])
    i=i+1
'''
'''
l=(1,4,9,16,25,36,49,64,81,100,36)
x=36
i=0
while i<len(l):
    if(l[i]==x):
        print("Found at index ",i)
        break
    else:
        print("finding")
    i=i+1
'''
i=0
while i<=5:
    if(i==3):
        i=i+1
        continue
    print(i)
    i=i+1

