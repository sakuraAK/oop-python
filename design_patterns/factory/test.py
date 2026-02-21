from towers.archer_tower import ArcherTower
from towers.cannon_tower import CannonTower
from towers.fireball_tower import FireballTower
from towers.ice_tower import IceTower
from tower_factory import TowerFactory

def use_towers_no_factory():
    for name in ["ArcherTower", "CannonTower", "FireballTower", "IceTower"]:
        if name == "ArcherTower":
            tower = ArcherTower()
            tower.fire()
            tower.take_damage()
        elif name == "CannonTower":
            tower = CannonTower()
            tower.fire()
            tower.take_damage()
        elif name == "FireballTower":
            tower = FireballTower()
            tower.fire()
            tower.take_damage()
        elif name == "IceTower":
            tower = IceTower()
            tower.fire()
            tower.take_damage()
        else:
            raise ValueError(f"No implementation for {name}")
        
        
def use_towers_with_factory():
    tower_factory = TowerFactory()
    for name in ["ArcherTower", "CannonTower", "FireballTower", "IceTower", "LightningTower"]:
        tower = tower_factory.create_tower(name)
        tower.fire()
        tower.take_damage()
    
        
# use_towers_no_factory()

use_towers_with_factory()