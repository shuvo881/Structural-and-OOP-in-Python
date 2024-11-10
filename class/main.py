
class Car: # class create

    def __init__(self, p, m, c):
        
        assert isinstance(p, float), "price is also float"
        assert p > 0, "price is no negative allow"
        
        self.price = p
        self.model = m
        self.color = c
    
 

a = Car(-10.2, 'AAA', 'Orange') # object creat

print(a.price) # aa


