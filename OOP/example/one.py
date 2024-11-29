from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, nm) -> None:
        self.area = None
        self.name = nm
    
    @abstractmethod
    def cal_area(self):
        pass

    def printer(self):
        print("Area of {} is {}".format(self.name ,self.area))


class Reactangle(Shape):
    def __init__(self, h, w, name):
        super().__init__(name)

        self.hight = h
        self.width = w

    def cal_area(self):
        self.area = self.hight * self.width
 

class Circle(Shape):
    def __init__(self, radius, nm):
        super().__init__(nm)
        self.r = radius

    def cal_area(self):
        self.area = 3.14 * self.r * self.r


class Squer(Reactangle):
    def __init__(self, d, nm):
        super().__init__(d, d, nm)
        


r = Reactangle(10, 20, "Reactangle")
r.cal_area()
r.printer()

# c = Circle(10, "Circle")
# c.cal_area()
# c.printer()

# s = Squer(10, "Squer")
# s.cal_area()
# s.printer()