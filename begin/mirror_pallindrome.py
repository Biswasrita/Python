
'''  #without function
    
s = input("Enter string:")
mirror_chars = ["8","1","0","a","h","i","m","o","t","u","w","x","y"]

is_palindrome = (s == s[::-1])  
is_mirror = all(c.lower() in mirror_chars for c in s)  

if is_palindrome and is_mirror:
    print("mirror palindrome.")
else:
   
    new_string = s + s[::-1]
    
    
    is_new_palindrome = (new_string == new_string[::-1]) 
    is_new_mirror = all(c.kower() in mirror_chars for c in new_string)  
    if is_new_palindrome and is_new_mirror:
        print("mirror palindrome after append")
    else:
        print("not a mirror palindrome.")
'''
'''
def check_mirror_palindrome():
   
    mirror_chars = ["8","1","0","a","h","i","m","o","t","u","w","x","y"]
    is_palindrome = (s == s[::-1])
    is_mirror = all(c in mirror_chars for c in s)

    if is_palindrome and is_mirror:
        print("mirror palindrome.")
    else:
        new_string = s + s[::-1]
        is_new_palindrome = (new_string == new_string[::-1])
        is_new_mirror = all(c in mirror_chars for c in new_string)

        if is_new_palindrome and is_new_mirror:
            print("mirror palindrome after append")
        else:
            print("not a mirror palindrome.")
s = input("Enter string: ")
print(check_mirror_palindrome())
'''

#with function
def is_palindrome(s):
    return s == s[::-1]

def is_mirror(s, mirror_chars):
    return all(c.lower() in mirror_chars for c in s)

def check_mirror_palindrome(s):
    mirror_chars = ["8","1","0","a","h","i","m","o","t","u","w","x","y"]
    
    if is_palindrome(s) and is_mirror(s, mirror_chars):
        return "mirror palindrome."
    else:
        new_string = s + s[::-1]
        if is_palindrome(new_string) and is_mirror(new_string, mirror_chars):
            return "mirror palindrome after append"
        else:
            return "not a mirror palindrome."
s = input("Enter string: ")
print(check_mirror_palindrome(s))


