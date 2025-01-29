class A:
    def __init__(self):
        print("Inside class A constructor")
    
    def hello(self,x):
        print("inside class A ....",x)


class B(A):
    
    ### although class A has a same function bu the object is created for class B so it will access its function first by default
    def hello(self,x):
        print("inside class B ....",x)


obj = B()
obj.hello("hello")
        