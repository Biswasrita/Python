'''
set1={10,True,"Jenny",11.5,1,10}#as there are duplicate of 10..so the length of the set is 5 not 6
set2={1,2,10,-10,0,53}
print(set2)#it's unchangeable
#indexing is not possible
#set2={}#dictionary
set2=set() #to create an empty set
print(type(set1))
print(type(set2))
set1.add(99)
print(set1)
print(len(set1))
set1.remove(10)
print(set1)
set1.pop()#remove an random number
print(set1)
'''
#operations on sets
set1={"Ram","Shyam","Jenny"}
set2={"Jenny","Jiya","Akash"}
set3={"Ankur","Pradeep"}
print(set1.union(("MOhan","Jenny")))
#print(set1.union(set2))
print(set1 | set2 | set3)
#set2.union(set1)

