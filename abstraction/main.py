

from abc import ABC, abstractclassmethod

class Person(ABC):
    
    def __init__(self, nam, age, dg):
        self.deg = dg # public
        self._name = nam # protected
        self.__age = age # private
    
    def __get_age(self):
        return self.__age
    
    @abstractclassmethod
    def get(self):
        return self.__get_age()
            
    
p = Person('Shuvo', 20, 'BSc')

x = p.get()
print(x)

"""
p = {
    deg:'BSc'
    _name: 'Shuvo'
    __age: 20
}

print(p.deg)
    
"""
