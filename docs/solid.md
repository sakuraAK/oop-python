# SOLID Principles

---

## Why SOLID Matters

As programs grow, they often become:
- Hard to understand
- Hard to change
- Easy to break

The **SOLID principles** are five guidelines that help us:
- Write flexible code
- Reduce bugs
- Make changes safely
- Work better in teams

> SOLID is about **design quality**, not syntax.

---

# S — Single Responsibility Principle (SRP)

## Definition

> A class should have **one reason to change**.

This means:
- One class = one job
- Each class focuses on **one responsibility**

---
## ❌ Problem Example (Too Many Responsibilities)

```python
class Library:
    def add_book(self, book):
        pass

    def save_to_file(self, filename):
        pass

    def send_email_notification(self):
        pass
```
Why this is bad:
- Business logic
- File I/O
- Notifications
are mixed together
- Any change affects the whole class

## ✅ Better Design
```python
class Library:
    def add_book(self, book):
        pass


class LibraryStorage:
    def save(self, library):
        pass


class NotificationService:
    def notify(self, message):
        pass
```
## Summary
- SRP improves readability
- Easier testing
- Smaller classes are easier to reuse
- SRP does not mean “only one method”

# O — Open/Closed Principle (OCP)

## Definition

> Software entities should be open for extension but closed for modification.


---
## ❌ Problem Example (If/Else Explosion)

```python
def calculate_fine(book_type):
    if book_type == "regular":
        return 2
    elif book_type == "rare":
        return 10
```
Why this is bad:
- Adding a new type requires changing existing code.


## ✅ Better Design
```python
from abc import ABC, abstractmethod

class FinePolicy(ABC):
    @abstractmethod
    def calculate(self):
        pass


class RegularFine(FinePolicy):
    def calculate(self):
        return 2


class RareBookFine(FinePolicy):
    def calculate(self):
        return 10
```
## Summary
- New behavior = new class
- Existing code stays untouched

# L — Liskov Substitution Principle (LSP)

## Definition

> Subclasses must be usable where their base class is expected.

> If it looks like a Book, it should behave like a Book.
---
## ❌ Problem Example (If/Else Explosion)

```python
class Book:
    def borrow(self):
        pass

class ReferenceBook(Book):
    def borrow(self):
        raise Exception("Cannot be borrowed")
```
Why this is bad:
- This breaks expectations.


## ✅ Better Design
```python
class Book:
    def borrow(self):
        pass


class ReferenceBook(Book):
    def borrow(self):
        print("Used in library only")
```
Alternatievly:
- Separate class hierarchy
- Or use composition

## Summary
- Subclasses should not surprise users
- Avoid weakening behavior
- LSP violations cause hidden bugs

# I — Interface Segregation Principle (ISP)

## Definition

> Clients should not be forced to depend on methods they do not use.

---
## ❌ Problem Example (If/Else Explosion)

```python
class BookActions:
    def borrow(self): pass
    def download(self): pass
```
Why this is bad:
- EBooks don’t need borrow().
- Physical books don’t need download().


## ✅ Better Design
```python
class Borrowable:
    def borrow(self): pass


class Downloadable:
    def download(self): pass
```

## Summary
- Small interfaces are better
- Improves clarity
- Easier to implement and test


# D — Dependency Inversion Principle (DIP)

## Definition

> High-level modules should not depend on low-level modules.
Both should depend on abstractions.

---
## ❌ Problem Example (If/Else Explosion)

```python
class Library:
    def __init__(self):
        self.storage = JsonStorage()
```
Why this is bad:
- Library is locked to JSON storage.


## ✅ Better Design
```python
class Storage:
    def save(self, data): pass


class JsonStorage(Storage):
    def save(self, data): pass


class Library:
    def __init__(self, storage):
        self.storage = storage
```

## Summary
- Easier to swap implementations
- Enables testing with mocks
- Reduces coupling

# How SOLID Principles Work Together
| Principle | Supports                 |
| --------- | ------------------------ |
| SRP       | Smaller, focused classes |
| OCP       | Safe extension           |
| LSP       | Reliable inheritance     |
| ISP       | Cleaner interfaces       |
| DIP       | Loose coupling           |

# Common Pitfalls
- Applying all SOLID rules at once
- Over-abstracting too early
- Adding patterns without a problem
- Confusing SOLID with “more classes”
> Remember: SOLID is not about writing more code.
It’s about writing code that survives change.

# Most Importantly
If your code:
- Is easy to read
- Is easy to change
- Does not break when extended

**Then you are already following SOLID. Good Job!**