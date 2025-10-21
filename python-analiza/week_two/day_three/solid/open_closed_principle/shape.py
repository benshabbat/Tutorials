from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for all shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        print("Calculating area")
        
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self):
        return 3.14159 * self.radius ** 2
    
    
class Square(Shape):
    def __init__(self, side: float):
        self.side = side
        
    def area(self):
        return self.side * self.side    
    
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height