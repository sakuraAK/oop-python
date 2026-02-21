from .tower import Tower
class CannonTower(Tower):
    def fire(self):
        print("Canon tower does: Kaa-boom!")

    def take_damage(self):
        print("Cannon tower taking damage...")