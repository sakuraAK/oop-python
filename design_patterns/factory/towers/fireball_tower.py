from .tower import Tower
class FireballTower(Tower):
    def fire(self):
        print("Fire tower goes: Whooshhhh")

    def take_damage(self):
        print("Fireball tower taking damage...")