
class A:
    g = 10

    def abc(self):
        print("Hello")

class B:

    def abc(self):
        print("Hello World")

class C(B, A):

    pass


c = C()
print(C.mro())

# orm
# mro