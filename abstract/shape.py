"""
Implement shapes (Rectangle, Square)

"""
from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(self, color):
        self.__color = color
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimiter(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} of color {self.__color}"
    
    @abstractmethod
    def draw(self):
        pass
    

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height
    
    def __str__(self):
        return super().__str__() + f"\nArea: {self.area()}; Perimeter: {self.perimiter()}"
    
    def area(self):
        return self.__height * self.__width
    
    def perimiter(self):
        return 2 * (self.__height + self.__width)
    
    def draw(self):
        return super().draw()


class  Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)



rectangle = Rectangle("red", 10, 15)


