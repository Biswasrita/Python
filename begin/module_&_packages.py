'''
import number_check as nc
#if __name__=="__main__":
n=int(input("Enter number:"))
prime=nc.is_prime(n)
pallindrome=nc.is_pallindrome(n)
print(f"Prime:{prime}\nPallindrome:{pallindrome}")
'''

import numpy as np
m=int(input("Enter no. of rows:"))
n=int(input("Enter no. of columns:"))
a=np.matrix(eval(input(f"Enter {m} x{n} matrix:")))
b=np.random.randint(1,20,size=(n,m))
c=np.matmul(a,b)
print(c)    