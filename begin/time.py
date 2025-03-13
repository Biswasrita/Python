n=input("Enter time:")
time=n.split(":")
if time[2][-2:]=="PM" and time[0]!="12":
    time=str(int(time[0])+12)
if time[2][-2:]=="AM" and time[0]=="12":
    time[0]="00"
time=":".join(time)[:-2]
print(time)
