class A:
    def abc(self):
        print("Hello")

class B(A):
    def abc(self):
        print("Hello World")


a = A()
b = B()

# a.abc()
b.abc()


