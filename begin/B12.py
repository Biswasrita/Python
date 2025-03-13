#import random
#a=random.randint(1,3)#we get 1,2,3
#a=random.randrange(1,3)#we get 1,2
#a=random.random()#floating point number(by default take 0-1 range)
#a=random.uniform(1,3)
#l=[2,4,78,45,17]
#a=random.choice(l)
#print(a)
#random.shuffle(l)#shuffle the list
#print(l)
'''
import random
side_of_coin=random.randint(0,1)
print(side_of_coin)
if side_of_coin==0:
    print("Tails")
else:
    print("Heads")
'''
'''
import random
name=['Tunai','Titin','Rohan','Abir']
a=random.choice(name)
print(a,"will pay the bill")
'''
import random
name=input("Enter name separated by coma:")
words=name.split(",")
length=len(words)
a=random.randint(0,length-1)
print(words[a],"will pay the bill")
