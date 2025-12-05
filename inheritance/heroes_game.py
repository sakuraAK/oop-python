import random

# Base class: Character
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {amount} damage! Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        # Default attack (will override in subclasses)
        print(f"{self.name} attacks {other.name}, but it's not very effective...")
        other.take_damage(1)


"""
Create a Warrior class
 - Inherits from Character
 - Has a special attack: power_strike()
 - Deals 5 damage
"""
class Warrior(Character):
    def power_strike(self, other: Character):
        print(f"{self.name} performes power strike attack on {other.name}")
        other.take_damage(5)
        
    def attack(self, other):
        if random.randint(0, 10) > 7:
            self.power_strike(other)
        else: 
            print(f"{self.name} attacks {other.name}, and deals some real damage")
            other.take_damage(3)


"""
Create a Mage class
 - Inherits from Character
 - Has a special attack: cast_spell()
 - Costs mana (add a mana attribute)
 - Deals 7 damage
"""
class Mage(Character):

    def __init__(self, name, health):
        super().__init__(name, health)
        self.__mana = random.randint(10, 100)
    
    def cast_spell(self, other: Character, spell_book=None):
        if self.__mana < 5:
             print(f"{self.name} tried to cast a spell on {other.name} but has not enough mana")
        else:
            current_spell = ""
            if not spell_book == None:
                current_spell = spell_book.use()
                
            print(f"{self.name} casts a {current_spell} spell on {other.name}")
            other.take_damage(7)
            self.__mana -= 5
    
    def attack(self, other):
        if random.randint(0, 10) > 7:
            self.cast_spell(other)
        else:
            print(f"{self.name} attacks {other.name}, and deals a moderate damage")
            other.take_damage(2)

"""
Override default attack
 - Warrior deals 3 damage
 - Mage deals 2
"""

"""
Add a new Character - Archer
"""

"""
Implement fight loop between warrior and mage
"""



if __name__ == "__main__":
    warrior = Warrior("Brut", 10)
    mage = Mage("Misterio", 7)

    while warrior.is_alive() and mage.is_alive():
        mage.attack(warrior)
        if not warrior.is_alive():
            break
        warrior.attack(mage)

    if warrior.is_alive():
        print("Warrior won")
    else:
        print("Mage has won")

