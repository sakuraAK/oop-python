"""
Import player from player
Add spell book class
Add cast spell method
"""
import sys
sys.path.append("../")

from inheritance.heroes_game import Mage, Warrior


class SpellBook:
    def __init__(self, spell_name):
        self.__spell_name = spell_name
        
    def use(self):
        return self.__spell_name



spell_book = SpellBook("fire")

mage = Mage("Dark One", 100)
warrior = Warrior("Brave One", 200)

mage.cast_spell(warrior, spell_book)

spell_book = SpellBook("Ice")
mage.cast_spell(warrior, spell_book)