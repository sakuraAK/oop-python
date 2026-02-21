from .tower import Tower

class LightningTower(Tower):
    def fire(self):
        print("Ligtning tower does: Pshhh")

    def take_damage(self):
        print(f"{self.__class__.__name__} tower taking damage...")