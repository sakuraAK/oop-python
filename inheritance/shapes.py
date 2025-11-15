"""
Implement shapes (Rectangle, Square)

"""

class Shape:
    
    def __init__(self, color):
        self.__color = color
    
    def area(self):
        raise NotImplementedError("Child class needs to implement this!")
    
    def perimiter(self):
         raise NotImplementedError("Child class needs to implement this!")
    
    def __str__(self):
        return f"{self.__class__.__name__} of color {self.__color}"
    

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
    


class  Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)



sq = Square("blue", 10)

print(sq)
