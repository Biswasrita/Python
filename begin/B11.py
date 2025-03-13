list=[1,4,5,7]#list is mutable
print(len(list))
list.append(45)
print(list)
list.insert(3,17)
print(list)
list[0]=18
print(list)
list[0:2]=[100,102,103]
print(list)
list.remove(5)
print(list)
list.pop()
print(list)
list.pop(2)#pop()delete the index
print(list)
