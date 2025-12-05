"""
Create a base class Enemy with a method attack().
Create three enemies:

Zombie
Dragon
Skeleton
"""
import time

class Enemy:
    def attack(self):
        print(f"{self.__class__.__name__} attacks")
        
        
class Zombie(Enemy):
    pass

class Dragon(Enemy):
    def attack(self):
        print(f"{self.__class__.__name__} attacks from above")
        
class Skeleton(Enemy):
    pass


enemies = [Zombie(), Dragon(), Skeleton()]

while True:
    time.sleep(5)
    for enemie in enemies:
        enemie.attack()
        
    # adds new enemies
    enemies.append(Zombie())
    
    
