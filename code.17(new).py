Name=['Titin','Tunai','Diya','Papan','Piku','Titli','Tinni','Rohan','Abir','Bubai']
print(f"The 1st list:{Name}")
Fees=[100,90,150,200,95,250,120,99,230,260]
print(f"The 1st list:{Fees}")
mf=max(Fees)
print(f"The maximum fees:{mf}")
p=Name[Fees.index(mf)]
print(f"The maximum amount is paid by:{p}")
total1=sum(Fees)
avg1=total1/10
print(f"The average of fees:{avg1}")
Name.remove('Rohan')
Name.remove('Abir')
print(f"The final list of persons:{Name}")
Fees.remove(99)
Fees.remove(230)
print(f"The final list of fees payment:{Fees}")
total2=sum(Fees)
avg2=total2/10
difference=avg1-avg2
print(f"The difference of avg amount:{difference:.2f}")




