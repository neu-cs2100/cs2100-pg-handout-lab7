"""
Please implement the methods and constructors in these stub classes.
"""


class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self) -> str:
        self.is_running = True
        return f"{self.make} {self.model} is now running"
    
    def stop(self) -> str:
        self.is_running = False
        return f"{self.make} {self.model} has stopped"

"""The stub classes for you to fill out:"""

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int):
        pass
    
    def honk(self) -> str:
        return "Beep beep!"

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, engine_size: int):
        pass
    
    def wheelie(self) -> str:
        if self.is_running:
            return "Doing a wheelie!"
        return "Can't do wheelie - motorcycle not running"