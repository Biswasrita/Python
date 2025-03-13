def is_prime(n):
    if n<2:
        return False
    for i in range(2,int (n**0.5)+1):
        if n%i==0:
            return False
    return True
def is_pallindrome(n):
    return n==n[::-1]
import numbercheck as nc
def main():
    num=eval(input("Enter integer:"))
    prime=numberCheck.is_prime(num)
    pallindrome=numberCheck.is_pallindrome(num)
    print(f" is {num} prime?{prime}")
    print(f" is {num} pallindrome?{pallindrome}")
    
