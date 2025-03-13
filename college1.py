import numpy as np
m=int(input("Enter no. of rows for matrix A:"))
n=int(input("Enter no. of columns for matrix A(and rows for matrix B):"))
A=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(int(input(f"Enter element [{i+1}][{j+1}] of matrix A:")))
    A.append(row)
B=np.random.randint(1,21,size=(n,m))
C=np.matmul(A,B)
print("Matrix A:")
print(np.array(B))
print("\nMatrix B:")
print(B)
print("Matrix C(A*B):")
print(C)

