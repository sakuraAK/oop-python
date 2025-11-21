# Abstract Classes & Interfaces

## 1. What Is an Abstract Class?

An abstract class is a class that cannot be instantiated on its own.
It defines a template for other classes to follow.

Key ideas:
- Contains abstract methods (methods with no implementation)
- Child classes must implement those methods
- Ensures consistent structure across subclasses
- Useful when you want to enforce a shared API

In Python, abstract classes are created using:
```python
from abc import ABC, abstractmethod
```
## 2. Python Abstract Class Example
```python
from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def attack(self):
        pass   # no implementation here

    @abstractmethod
    def take_damage(self, amount):
        pass

# This class defines the required behaviors for all enemies.
# Subclasses must implement all abstract methods:

class Orc(Enemy):
    def attack(self):
        print("Orc swings a club!")

    def take_damage(self, amount):
        print(f"Orc takes {amount} damage!")

class Troll(Enemy):
    def attack(self):
        print("Troll throws a rock!")

    def take_damage(self, amount):
        print(f"Troll grunts and takes {amount} damage!")
```

**Important:**  Abstract classes cannot be instantiated.

## 3. What Is an Interface?

Python does not have a native “interface” keyword like Java or C#.

But an interface is conceptually:
- A class with only abstract methods
- No attributes (except constants)
- No implementation details
- Just a contract of what methods must exist

In Python, interfaces are usually implemented by:
- Abstract classes with only abstract methods, or
- Protocols (Python 3.8+) from typing module
### Interface-Style Example (Abstract class)
```python
from abc import ABC, abstractmethod

class WeaponInterface(ABC):

    @abstractmethod
    def use(self):
        pass
# It has no attributes
# It has no implemented logic
# It only defines required methods

# Different weapons implement the interface

class Sword(WeaponInterface):
    def use(self):
        print("Sword slash!")

class Bow(WeaponInterface):
    def use(self):
        print("Arrow shot!")

class Wand(WeaponInterface):
    def use(self):
        print("Magic spark!")
```