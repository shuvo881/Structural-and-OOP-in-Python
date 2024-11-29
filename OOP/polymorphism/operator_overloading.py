
class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a # 10 + 20 = 30
    
    def __sub__(self, other):
        return self.a - other.a



aa = A(10) # aa.a = 10
bb = A(20) # bb.a = 20

c = aa - bb
# c = aa + bb
# c = bb.__add__(bb)

print(c)

# cc = aa + bb


