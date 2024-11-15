class A:
    def __init__(self, a):
        self.g = a

    def abc(self):
        print("Hello")

class B(A):
    def __init__(self, cc):
        super().__init__(cc)

    def abc(self):
        print("Hello World")
    
class C(B):
    def __init__(self, c):
        super().__init__(c)
    
    def abc(self):
        print("Hello World 2")


a = A(10)
a.abc()

b = B(20)
b.abc()

c = C(30)
c.abc()
