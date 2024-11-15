
# def outer(fun):
    
#     def inner():
#         print('inner')
#         fun()
    
#     return inner


# def original():
#     print('original')
    


# f = outer(original)

# f()


def smar_div(fun):
    
    def inner(a, b):
        if b == 0:
            print('no div')
            return
        fun(a, b)
    
    return inner

@smar_div
def div(a, b):
    print(a / b)
    
# f = smar_div(div)
# f(10, 2)
div(10, 2)
# div(10, 0)
