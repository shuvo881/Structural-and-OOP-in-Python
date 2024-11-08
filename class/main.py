
class Car: # class create

    def __init__(self, p, m, c):
        self.price = p
        self.model = m
        self.color = c
    
 

a = Car(10, 'AAA', 'Orange') # object create
b = Car(20, 'BBB', 'Blue') # object create



print(a.color) #Orange
print(b.model) #BBB

