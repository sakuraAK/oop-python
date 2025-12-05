"""
Composition
Create class for smartphone with status method
Create batter class with get_level method
"""

class Battery:
    def __init__(self):
        self.__capacity = 100

    def get_level(self):
        return self.__capacity
    

class Smartphone:
    
    def __init__(self):
        self.__battery = Battery()
        
    def get_status(self):
        print(f"Battery at {self.__battery.get_level()}% capacity")
        

phone = Smartphone()

phone.get_status()