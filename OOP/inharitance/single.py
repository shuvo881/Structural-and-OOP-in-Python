class A:
    def __init__(self, g):
        self.g = g

    def abc(self):
        print("Hello")

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.f = b
        
    def abc(self):
        super().abc()
        print("Hello World")





obj_m = B(3.2, 2.3)
obj_m.abc()

# a = A()
# b = A()
# print(a.g)