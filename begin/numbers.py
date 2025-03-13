#Consider a range of NUMBERS. If the NUMBER exists at the very end of its squared value, print the NUMBER.



for num in range(10, 1000):
    square = num * num
    n=str(num)
    s=str(square)
    if s.endswith(n):
        print(num)
        
