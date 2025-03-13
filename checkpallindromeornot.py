def is_pallindrome(n):
    return n==n[::-1]
num=(input("Enter:"))
if is_pallindrome(num):
    print("Pallindrome")
else:
    print("Not pallindrome") 
