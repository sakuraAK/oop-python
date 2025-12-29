# Final Project OOP — Smart Library Management System

---

## Project Overview

In this final project, you will build a **Smart Library Management System** using **Object-Oriented Programming (OOP)** in Python.

The goal is to design a small but realistic application that demonstrates all the concepts you have learned in this course, including object modeling, relationships, file storage, documentation, and (optionally) automated testing.

This project prioritizes **clear structure, correctness, and good design practices** over advanced Python features.

---

## Concepts Covered

This project summarizes **everything we covered in class**:

- Encapsulation (private attributes, properties)
- Inheritance
- Relationships (association, aggregation, composition)
- Polymorphism
- Lists and dictionaries of objects
- Abstract classes and interface-like design
- Magic methods (`__str__`, `__eq__`, etc.)
- Error handling (`try/except`, custom exceptions)
- File I/O
- Saving and loading application data using JSON
- Documentation using docstrings
- Automated testing using pytest (optional)

---

## Scenario

You are developing software for a **small public library** that needs to:

- Store books
- Register members
- Manage borrowing and returns
- Persist data between program runs
- Be readable, maintainable, and testable

---


# Step-by-step implementation walkthrough

## Step 1 — Book Hierarchy (Abstraction & Inheritance)

### Abstract Base Class: `Book`

Create an abstract class `Book` that defines the common structure of all books.

**Attributes:**
- `_id`
- `_title`
- `_author`

**Required methods:**
- `borrow()`
- `return_book()`
- `to_dict()`

The `Book` class:
- Must **not** be instantiated directly
- Acts as an interface
- Enforces consistent behavior across subclasses

---

### Subclasses

#### `PhysicalBook`
Additional attribute:
- `_available_copies`

#### `EBook`
Additional attribute:
- `_file_size_mb`

Each subclass must:
- Implement `borrow()`
- Implement `return_book()`

Concepts used:
- Inheritance
- Method overriding
- Polymorphism

---

## Step 2 — Member Class

Represents a library member.

**Attributes:**
- `_member_id`
- `_name`
- `_borrowed_books` (list of `Book` objects)

**Methods:**
- `borrow_book(book)`
- `return_book(book)`
- `to_dict()`

Rules:
- Members cannot borrow the same book twice
- Members cannot return books they do not have

Concepts used:
- Encapsulation
- Lists of objects
- Association

---

## Step 3 — Loan Class (Composition)

Represents a borrowing event.

**Attributes:**
- `book`
- `member`
- `date_borrowed`

Rules:
- A `Loan` cannot exist without a book and a member
- Created only when borrowing succeeds

Concepts used:
- Composition
- Object collaboration

---

## Step 4 — Library Class (System Controller)

Coordinates all library operations.

**Attributes:**
- `_books` → `{book_id: Book}`
- `_members` → `{member_id: Member}`
- `_loans` → `list[Loan]`

**Methods:**
- `add_book(book)`
- `add_member(member)`
- `borrow_book(member_id, book_id)`
- `return_book(member_id, book_id)`
- `save_to_file(filename)`
- `load_from_file(filename)`

Concepts used:
- Dictionaries of objects
- Aggregation
- Separation of concerns

---

## Step 5 — Magic Methods

Implement **at least two** magic methods.

Suggested:
- `__str__()` — readable output
- `__eq__()` — compare objects by ID

Used for:
- Printing objects
- Comparing objects
- Debugging

---

## Step 6 — Error Handling

Create and use **custom exceptions**.

Suggested:
- `BookNotAvailableError`
- `BookNotFoundError`
- `MemberNotFoundError`

Use `try/except` blocks to:
- Prevent crashes
- Display meaningful error messages

Concepts used:
- Custom exceptions
- Defensive programming

---

## Step 7 — JSON Persistence (File I/O)

The application must:
- Save all books, members, and loans to a JSON file
- Load them back correctly

Rules:
- Objects must be converted to dictionaries
- JSON must contain only basic data types
- Loaded data must recreate objects correctly

Concepts used:
- File I/O
- Serialization
- Object reconstruction

---

## Step 8 — Documentation with Docstrings (Required)

❗ **All classes and public methods MUST be documented using docstrings.**

Each docstring should explain:
- What the class or method does
- Parameters
- Return values (if any)
- Exceptions raised (if applicable)

Example:

```python
class Book:
    """
    Represents a generic book in the library.

    This class defines the common interface for all book types.
    """
```

## Step 9 — Automated Testing with pytest (Optional, Bonus)

Automated testing is **optional**, but students who implement tests will receive **bonus credit**.

The goal of testing is to verify that your **Library API works correctly** and that changes do not break existing behavior.

### What to Test

Focus on **behavior**, not implementation details.

Suggested test cases:
- Adding a book to the library
- Adding a member
- Borrowing a book (successful case)
- Borrowing a book that is unavailable
- Returning a book
- Saving data to JSON and loading it back correctly

### Guidelines

- Use `pytest`
- Write tests that interact with the `Library` class
- Use `pytest.raises()` to test error cases
- Keep tests small and focused
- Place tests in a `tests/` directory

Testing is considered **advanced** at this stage — partial implementations are acceptable.

---

## Step 10 — Console Menu Interface

Create a simple **text-based menu** for interacting with the system.

Example menu:
1. Add book
2. Add member
3. Borrow book
4. Return book
5. List books
6. List members
7. Save library
8. Load library
9. Exit

### Rules

- The menu must **not contain business logic**
- The menu should only call methods on the `Library` class
- Invalid input must be handled gracefully
- Errors should display friendly messages, not stack traces

❗ The menu exists to **demonstrate usage**, not to hold application logic.

---

## Submission Requirements 

❗ This is **individual** project. Group or identical submissions will not be accepted.

❗ You **must** submit your project using **Git and GitHub**.

Requirements:
- Create or use an existing Git repository for your project
- Push the repository to GitHub
- Commit your work regularly
- Meaningful commit messages are expected

---

### Repository Structure (Suggested)
```
project-root/
├── library/
│ ├── book.py
│ ├── member.py
│ ├── loan.py
│ └── library.py
├── tests/ # optional
├── main.py
├── README.md
└── data.json # created by the program
```

---

## README.md Requirements

Your `README.md` file must include:

- Project title and description
- How to run the application
- Example usage
- How to save and load data
- How to run tests (if implemented)

---

## How This Project Will Be Evaluated

Your project will be graded based on:

* Correct use of OOP concepts
* Functionality
* Code correctness, simplicity, and readability
* Project structure

❗  Python advanced features are **not** the main focus.

---

## Final Notes

This project is meant to be **achievable and confidence-building**.

Keep it simple, follow the requirements, and focus on showing what you’ve learned.

Good luck! 