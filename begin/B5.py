'''
n=input("Enter string:")
words=n.split()
print(words)
L=max(len(words))
print("max:",L)
'''
'''
n=input("Enter string:")
s=n.split()
print(s)
L=" "
for i in s:
    if len(i)>len(L):
        L=i
print("Longest Word:",L)
'''


n=input("Enter string:")
words=n.split()
max_length=0
for i in words:
   if len(i)>max_length:
        max_length=len(i)
        

for i in words:
   if len(i)==max_length:
        print("Longest words:",i)



