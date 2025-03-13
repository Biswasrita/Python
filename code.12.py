Numbers=[4,5,87,14,17,8,1,2,3]
print(f"The given list is:{Numbers}")
Prime_Numbers=[]
for i in Numbers:
    if (i>1):
        prime=True
        for n in range(2,i):
            if(i%n==0):
                prime=False
                break
        if (prime):
            Prime_Numbers.append(i)
print(f"The Prime Numbers from list:{Prime_Numbers}")
Total=sum(Prime_Numbers)
print(f"The sum of Prime Numbers:{Total}")