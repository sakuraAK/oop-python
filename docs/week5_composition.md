# Composition & Class Relationships

## 1. What Is Composition?

**Composition** is an object-oriented programming technique where a class is **built from other classes**.

This is known as a **HAS-A relationship**:

- A Car *has an* Engine  
- A Player *has a* Weapon  
- A House *has* Rooms  

Composition models real-world “part-of” structures.

### Why Use Composition?
- Promotes clean modular design  
- Components can be reused  
- Encourages flexibility and easier maintenance  
- Avoids deep and rigid inheritance chains  

---

## 2. Composition Example (Python)

```python
class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def drive(self):
        self.engine.start()
        print("Car is now driving!")
```

## 3. Types of Class Relationships
### A. Inheritance (IS-A Relationship)

Used when one class is a specialized version of another:
- Dog is an Animal
- SavingsAccount is a BankAccount

```python
class Animal:
    def speak(self):
        print("Generic sound")

class Dog(Animal):
    pass
```
### B. Composition (HAS-A Relationship)
Used when one class contains another as a component.
```python
class Engine: pass

class Car:
    def __init__(self):
        self.engine = Engine()
```
### C. Aggregation (Weaker HAS-A)
The whole and its parts can exist independently.
```python
class Student: pass

class Classroom:
    def __init__(self, students):
        self.students = students  # students exist independently
```
### D. Association
Two classes interact, but neither owns the other.
```python
class Doctor: pass
class Patient: pass
```
## 4. Composition vs Inheritance
Use Inheritance When:
- A class is a clear subtype of another
- Shared behavior should be inherited
- Polymorphism is needed

Use Composition When:
- One object is a component of another
- You want flexibility and easy swapping of behavior
- Behavior is not a natural “is-a” relationship
- You want to avoid overly complicated inheritance trees

## 5. Summary

**Inheritance**: "is-a"

**Composition**: "has-a"

**Aggregation**: "has-a but independent"

**Association**: "works-with"

Composition is often preferred because it results in flexible, modular, and maintainable designs.