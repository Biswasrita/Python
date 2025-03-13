class B:
    def __init__(self,n):
        self.val1= n
        print("Class B object is created")
    def show(self):
        print("Showing Class B with", {self.val1})
    def __del__(self):
        print("Object deleted")
b1=B(10)
b1.show()
b2=B(20)
b2.show()