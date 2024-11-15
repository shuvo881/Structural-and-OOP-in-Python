# 1, 2, 3, 4, 5

# i = 6
def count(i):
    
    if i > 5: #6 > 5
        return
    
    print(i)
    count(i + 1)
    print('i: ',i)
    
    
    
    
count(1)