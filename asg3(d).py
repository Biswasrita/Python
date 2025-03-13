n=input("Enter a character:")
match n:
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("It is vowel")
    case _ if len(n)==1 and n.isalpha():
        print("It is consonant")
    case _ :
        print("Invalid Input")    