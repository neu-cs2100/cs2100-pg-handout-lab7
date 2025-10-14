import math

"""
Please implement the methods and constructors in these stub classes.
"""

class Shape:
    def __init__(self, name: str):
        self.name = name
    
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area method")
    
    def describe(self) -> str:
        return f"This is a {self.name}"


"""The stub classes for you to fill out:"""

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        pass
    
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        pass
    
    def area(self) -> float:
        pass
