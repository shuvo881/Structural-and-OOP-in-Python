class A:

    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c=0):
        print("Hello")
        return a + b + c
    

aa = A()
print(aa.add(3, 4))