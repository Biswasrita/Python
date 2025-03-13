a1=list(map(int,input("Enter 1st array:").split(',')))
a2=list(map(int,input("Enter 2nd array:").split(',')))

merge=a1+a2
sort=sorted(merge)
n=len(sort)
if n%2!=0:
    median=sort[n//2]
    print(median)
else:
    median=sum(sort)/(n)
    print(median)

