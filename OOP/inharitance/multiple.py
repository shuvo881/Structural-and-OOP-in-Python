
class __A:
    g = 10

    def abc(self):
        print("Hello")

class B:

    def abc(self):
        print("Hello World")

class C(B, __A):
    
    pass


c = C()
print(c.g)