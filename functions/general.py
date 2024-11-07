# No parameter with no return type

# def adder():
#     a = 10
#     b = 20
#     c = a + b
#     print('total: ', c)
    
    
# if __name__ == '__main__':
    
#     adder()



# No parameter with return type

# def adder() -> int:
#     a = 10
#     b = 20
    
#     c = a + b # 30.5
    
#     return a

# x = adder() # x = 30

# print(x)


# Parameter with no return type
# a = 10, b =20
# def adder(a: int, b: int):
#     c = a + b
#     print(c)

# # print(c)
# adder(10, 20)


# Parameter with return type
# a = 20 , b = 10
def adder(a:int, b:int=10) -> int: 
    c = a + b
    
    return c

y = adder(20, 30)

print(y)
