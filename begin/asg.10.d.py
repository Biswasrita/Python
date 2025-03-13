class F:
    def __init__(self,string):
        self.string=string
    def __sub__(self,other):
        other_chars=set(other.string)
        result=''.join([char for char in self.string if char not in other_chars])
        return result
x=F("Hello")
y=F("World")
result=x-y
print(result)