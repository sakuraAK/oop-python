from .tower import Tower

class ArcherTower(Tower):
    def fire(self):
        print("Tower shooting arrows")
    
    def take_damage(self):
        print(f"{self.__class__.__name__} taking damage")