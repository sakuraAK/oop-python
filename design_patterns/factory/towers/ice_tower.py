from .tower import Tower

class IceTower(Tower):
    def fire(self):
        print("Ice Tower shooting ice bolts")
    
    def take_damage(self):
        print(f"{self.__class__.__name__} taking damage")