#f1=open("MCKV.txt","w")
#f1.write("Welcome to Python")

import os
f1=open("BS.txt","r")
#print(f1.read())
print(len(f1.read()),"bytes")
#print(os.path.getsize("BS.txt"),"bytes")
f1.close()