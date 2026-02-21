from inspect import getmembers, isclass, isabstract
import towers
from towers.tower import Tower


class TowerFactory:
    def __init__(self):
        self.__towers = {}
        self.load_towers()
    
    def load_towers(self):
        classes = getmembers(towers, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, Tower):
                self.__towers[name] = _type
                
    def create_tower(self, name) -> Tower:
        if name in self.__towers:
            return self.__towers[name]()
        else:
            raise ValueError(f"Implmentation for {name} not found")
        
