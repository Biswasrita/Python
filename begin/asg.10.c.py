class A:
    
    def __init__(self):
        print("Class A object created")
    def show(self):
        print("Showing Class A")
    def __del__(self):
        print("Object deleted")
class B(A):
    def __init__(self,val1):
        self.val1= val1
        print("Class B object is created")
    def show(self):
        print(f"Showing Class B object having value {self.val1}")
class C(B):
    def __init__(self,val1,val2):
        super().__init__(val1)
        self.val2=val2
        print("Class C is created")
    def show(self):
        print("showing class C with",self.val1,self.val2)
x=C(10,20)
x.show()