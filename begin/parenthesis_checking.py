#finding the length of last word---
'''
input=input("Enter: ")
words=input.split()
n=len(words[-1])
print(n)
'''
#plus one
'''
digit=list(map(int,input("Enter number:").split()))
for i in range(len(digit)-1,-1,-1):
    if digit[i]<9:
        digit[i]+=1
        print(digit)
        break
    digit[i]=0
else:
    print([1]+digit)
'''
#finding the kth largest element
'''
n=int(input("Enter number of ekements u want to enter:"))
given=list(map(int,input("Enter number:").split()))

k=int(input("Enter k th largest number:"))
given.sort()
print(given)
print("The kth largest element:",given[k-1])
'''

#finding the kth largest element
'''
n=int(input())
k=int(input())
given=list(map(int,input().split()))
given.sort(reverse=True)
print(given[k-1])
'''

