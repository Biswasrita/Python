'''a=5
b=2


try:
    print("resource open")
    print(a/b)
    k=int(input("Enter number:"))
    print(k)
except Exception as e:
    print("Issue:",e)
else:
    print("Biswasrita")
finally:
    print("resource close")'''

def check_brackets(s):
    try:
        stack=[]
        for char in s:
            if char=="(":
                stack.append(char)
            elif char==")":
                if not stack:
                    raise ValueError("Brackets are not well formed")
                stack.pop()
               
    except ValueError as e :
        print(e)
        return False
    else:
        if stack:
            print("Brackets are not well formed")
            return False
        else:
            print("Brackets are well formed")
            return True
    finally:
        print("Done")
#if __name__=="__main__":
s=input("Enter expression:")
check_brackets(s)








