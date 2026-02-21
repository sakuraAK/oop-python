# Smart Library Management System

A Python-based object-oriented library management system demonstrating core OOP concepts including encapsulation, inheritance, polymorphism, composition, and persistence.

## Project Overview

This system allows a small public library to:
- Manage a collection of books (physical and e-books)
- Register and manage library members
- Handle book borrowing and returns
- Persist data to JSON files
- Provide a user-friendly console interface

## Features

- **Book Management**: Support for two book types with different borrowing rules
  - Physical Books: Limited copies with availability tracking
  - E-Books: Unlimited simultaneous borrowing
- **Member Management**: Register members and track their borrowing history
- **Borrowing System**: Complete lifecycle management (borrow, return, tracking)
- **Data Persistence**: Save and load library state via JSON
- **Error Handling**: Custom exceptions for domain-specific errors
- **Console Interface**: Interactive menu-driven interface

## Project Structure

```
final-project-sol/
├── library/
│   ├── __init__.py           # Package initialization
│   ├── book.py               # Book abstract class and subclasses
│   ├── member.py             # Member class
│   ├── loan.py               # Loan class (composition)
│   ├── library.py            # Main Library controller
│   └── exceptions.py         # Custom exceptions
├── tests/
│   └── test_library.py       # Unit tests (optional, bonus)
├── main.py                   # Console menu interface
├── README.md                 # This file
└── data.json                 # Persisted library data (created at runtime)
```

## OOP Concepts Demonstrated

### Encapsulation
- Private attributes with property accessors
- Controlled access to object state (e.g., `Member._borrowed_books`)

### Inheritance
- Abstract `Book` base class
- Concrete subclasses: `PhysicalBook`, `EBook`
- Polymorphic behavior through method overriding

### Polymorphism
- Different `borrow()` and `return_book()` implementations
- Works seamlessly with the `Library` interface

### Composition
- `Loan` class depends on `Book` and `Member` instances
- `Library` contains collections of books, members, and loans

### Relationships
- **Aggregation**: Library owns books and members (they can exist independently)
- **Composition**: Loans depend on books and members (cannot exist without them)

### Magic Methods
- `__str__()`: Readable object representation
- `__eq__()`: Object comparison by ID

### Abstract Classes
- `ABC` module for enforcing interface contracts
- Abstract methods: `borrow()`, `return_book()`, `to_dict()`

### File I/O & Serialization
- JSON persistence with type preservation
- Correct deserialization and object reconstruction

### Error Handling
- Custom exceptions with descriptive messages
- Try-except blocks for defensive programming

## How to Run

### Prerequisites
- Python 3.7 or higher
- No external dependencies required for basic functionality

### Running the Application

```bash
cd final-project-sol
python main.py
```

### Running Tests (Optional)
```bash
pytest tests/
```

## Usage Guide

### Main Menu Options

1. **Add Physical Book**: Add a new physical book with a set number of copies
2. **Add E-Book**: Add a new e-book with file size information
3. **Add Member**: Register a new library member
4. **Borrow Book**: Record a member borrowing a book
5. **Return Book**: Record a member returning a book
6. **List All Books**: Display all books in the library
7. **List All Members**: Display all registered members
8. **List Member's Borrowed Books**: Show books borrowed by a specific member
9. **Save Library to File**: Persist library state to JSON
10. **Load Library from File**: Restore library state from JSON
11. **Exit**: Quit the application

### Example Workflow

```
1. Add a Physical Book
   - ID: B001
   - Title: Python Programming
   - Author: John Doe
   - Copies: 3

2. Add an E-Book
   - ID: E001
   - Title: Design Patterns
   - Author: Jane Smith
   - File Size: 5.2 MB

3. Add a Member
   - ID: M001
   - Name: Alice Johnson

4. Borrow Book
   - Member ID: M001
   - Book ID: B001
   - Result: 2 copies of "Python Programming" remain available

5. Save Library
   - Saves to data.json

6. Return Book
   - Member ID: M001
   - Book ID: B001
   - Result: 3 copies of "Python Programming" available again

7. Load Library
   - Restores all data from data.json
```

## Data Persistence

### Save Format

The library saves to JSON with the following structure:

```json
{
  "books": [
    {
      "type": "PhysicalBook",
      "id": "B001",
      "title": "Python Programming",
      "author": "John Doe",
      "available_copies": 2
    },
    {
      "type": "EBook",
      "id": "E001",
      "title": "Design Patterns",
      "author": "Jane Smith",
      "file_size_mb": 5.2
    }
  ],
  "members": [
    {
      "member_id": "M001",
      "name": "Alice Johnson",
      "borrowed_books": ["B001"]
    }
  ],
  "loans": [
    {
      "book_id": "B001",
      "member_id": "M001",
      "date_borrowed": "2026-02-21"
    }
  ]
}
```

### Loading Data

The system automatically reconstructs:
- Book objects with their original types and states
- Member objects with their borrowed books lists
- Loan records linking all relationships

## Classes and Key Methods

### Book (Abstract)
- `borrow()`: Mark book as borrowed
- `return_book()`: Mark book as returned
- `to_dict()`: Serialize to dictionary

### PhysicalBook
- `available_copies`: Property tracking copies
- Raises `BookNotAvailableError` when borrowing with no copies

### EBook
- `file_size_mb`: Property for file size
- Always allows borrowing (unlimited copies)

### Member
- `borrow_book(book)`: Add book to borrowed list
- `return_book(book)`: Remove book from borrowed list
- Prevents duplicate borrowing of the same book

### Loan
- Represents a borrowing event
- Requires both book and member (composition)
- Records the date borrowed

### Library
- `add_book(book)`: Add book to library
- `add_member(member)`: Register new member
- `borrow_book(member_id, book_id)`: Process borrowing
- `return_book(member_id, book_id)`: Process return
- `save_to_file(filename)`: Persist to JSON
- `load_from_file(filename)`: Load from JSON

## Error Handling

The system uses custom exceptions for clear error messages:

- **`BookNotAvailableError`**: No copies available to borrow
- **`BookNotFoundError`**: Book ID not in library
- **`MemberNotFoundError`**: Member ID not registered
- **`InvalidOperationError`**: Invalid state change (e.g., returning unborrrowed book)

## Testing (Optional - Bonus)

Run pytest tests to verify functionality:

```bash
pytest tests/ -v
```

Tests cover:
- Adding books and members
- Successful borrowing
- Error cases (unavailable books, invalid returns)
- JSON persistence and loading
- Data integrity

## Design Principles

1. **Separation of Concerns**: Menu logic is separate from business logic
2. **Single Responsibility**: Each class has one clear purpose
3. **DRY (Don't Repeat Yourself)**: Shared functionality in base classes
4. **Defensive Programming**: Input validation and error handling throughout
5. **Clear Documentation**: Every class and method is documented with docstrings

## Limitations & Future Enhancements

### Current Limitations
- Single-threaded console interface
- No user authentication
- No fine system for overdue books
- No book search/filtering beyond listing

### Possible Enhancements
- Database persistence (SQLite, PostgreSQL)
- Due dates and fine calculations
- Book search and filtering
- Member history and statistics
- Multi-user support with authentication
- Web interface (Flask/Django)

## Author

Created as part of an OOP Python course demonstrating practical application of design principles.

## License

This project is provided as educational material.
