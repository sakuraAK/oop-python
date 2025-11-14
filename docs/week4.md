# 🗓️ Week 4

## Understanding `__init__` in Python  

### What Is `__init__`?

`__init__` is a **special method** in Python that runs **automatically** after an object is created.  
It is used to **initialize the object’s data** — to give the object its starting state.

Think of it like a **setup step** that prepares the object right after it comes into existence.

---

### Why `__init__` Is Not the Constructor

In many languages (Java, C++, etc.), the constructor is the method that **creates** the object.

But in Python:

### ✔ The real constructor is `__new__`  
- `__new__` creates the object in memory  
- Python calls this first  

### ✔ `__init__` only initializes the object  
- The object already exists before `__init__` runs  
- So technically, `__init__` is an **initializer**, not a creator

Python hides `__new__()` from beginners, so you mostly work with `__init__`.

---

### Simple Example of `__init__`

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # store name
        self.age = age        # store age

buddy = Dog("Buddy", 3)
```
### Example Showing the Difference (`__new__` vs `__init__`)
```python
class Example:
    def __new__(cls):
        print("Constructor (__new__) is running")
        return super().__new__(cls)

    def __init__(self):
        print("Initializer (__init__) is running")

obj = Example()
```

## Inheritance

### What Is Inheritance?

Inheritance is an OOP mechanism that allows one class to **reuse**, **extend**, or **modify** another class’s features.

- The class being inherited from → **Parent class** (or **Base class**)
- The class that inherits → **Child class** (or **Derived class**)

It helps:
- Reduce code duplication  
- Keep related classes organized  
- Model real-world "is-a" relationships  
- Extend existing functionality without rewriting everything  

---

### Basic Inheritance Example

```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):   # Dog inherits from Animal
    def bark(self):
        print("Woof!")
```

### Adding an __init__ in a Parent Class
```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I'm {self.name}")

class Student(Person):
    pass
```
Because Student doesn’t override __init__, it uses the parent’s version.

### Extending Behavior in a Child Class
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)     # call parent initializer
        self.student_id = student_id

```
### Overriding a Method
```python
class Animal:
    def sound(self):
        print("Some generic sound")

class Cat(Animal):
    def sound(self):   # override
        print("Meow!")

```
---
### When to Use Inheritance

Use inheritance when:

 - There is a clear **“is-a”** relationship
(e.g., Dog is an Animal, Student is a Person)

 - A child class can **reuse** most of the parent’s functionality

- You want to avoid **duplicating** code

Avoid inheritance when:

 - The relationship is **not “is-a”** (use composition instead)

- You only want to share small pieces of functionality
---
### Summary
Inheritance lets a child class reuse and customize the behavior of a parent class, helping you write cleaner and more organized code.