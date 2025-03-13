'''
def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(5,10)
 '''
'''
def calc_sum(a,b):
    return a+b
sum=calc_sum(8,4)
print (sum)
'''
'''
def ph():
    print("Hello")
ph()
ph()
'''

'''
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calc_avg(4,5,6)
 '''



'''
#WAF to print the length of a list
def len_list(L):
    return(len(L))
l=len_list(L=[4,5,7,8])
print("The length of list:",l)
'''
'''
#WAF to print the elements of a list in a single line(list is the parameter)
Number=["one","two","three"]
def pn(N):
    for i in N:
        print(i,end=" ")
pn(Number)
'''
'''
#WAF to find the factorial of n (n is the parameter)
n=int(input("Enter:"))
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("The factorial is:",calc_fact(n))
'''
'''
#WAF to convert USD to INR

def converter(n):
    inr=n*83
    print(n ,"USD=",inr,"INR")
converter(5)
'''
#WAF even odd
def eo(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
eo(5)








