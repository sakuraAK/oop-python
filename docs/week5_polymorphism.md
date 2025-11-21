# Polymorphism & Method Overriding

## 1. What Is Polymorphism?
Polymorphism means “many forms.”
In OOP, it allows different classes to respond to the same method call in different ways.

### Why It Matters:

- Makes code flexible
- Allows you to write code that works on general types
- Reduces duplication
- Is essential for building scalable systems (games, UI, simulations, etc.)
----

## 2. How Polymorphism Works in Python

Python supports dynamic polymorphism, meaning:

If two different classes have the same method name, Python will call the version based on the actual object type, not the variable type.
### Example 1 Basic Polymorphism
```python
class Warrior:
    def attack(self):
        print("Warrior swings a sword!")

class Archer:
    def attack(self):
        print("Archer shoots an arrow!")

# Polymorphic behavior
def battle_attack(character):
    character.attack()   # Same method name, different behavior

battle_attack(Warrior())
battle_attack(Archer())

```
**Key Idea**: battle_attack() does not need to know the class—it only expects .attack() to exist.
### Example 2 — Polymorphism via Inheritance (Method Overriding)
```python
class Enemy:
    def attack(self):
        print("Enemy attacks!")

class Orc(Enemy):
    def attack(self):
        print("Orc attacks brutally!")

class Goblin(Enemy):
    def attack(self):
        print("Goblin attacks sneakily!")

enemies = [Orc(), Goblin()]

for enemy in enemies:
    enemy.attack()

```
