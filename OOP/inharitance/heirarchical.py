
class A:
    g = 10

class B(A):
    pass

class C(A):
    pass

class D(A):


    def printer(self):
        print(self.g)


# d = D()
# d.printer()
b = B()
print(b.g)