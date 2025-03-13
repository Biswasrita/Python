
def unique_output(n):
    outputs=set()
    prev_output=1
    for i in range(1,n+1):
        output=prev_output*i
        if output<=n:
            outputs.add(output)
            prev_output=output
    return sorted(list(outputs))
n=int(input("Enter:"))
print("Unique outputs:",unique_output(n))