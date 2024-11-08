
def counter():
    yield 1
    yield 2
    yield 3
    
fun = counter()

print(next(fun))
print(next(fun))
print(next(fun))