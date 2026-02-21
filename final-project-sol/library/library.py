"""
Library module for the Smart Library Management System.

Provides the main Library class that coordinates all library operations.
"""

import json
from .book import PhysicalBook, EBook
from .member import Member
from .loan import Loan
from .exceptions import (
    BookNotAvailableError,
    BookNotFoundError,
    MemberNotFoundError,
    InvalidOperationError,
)


class Library:
    """
    Represents a library and manages all library operations.

    The Library class is the main system controller that coordinates books, members, and loans.
    It handles borrowing, returning, persistence, and data queries.

    Attributes:
        _books (dict): Dictionary mapping book IDs to Book objects.
        _members (dict): Dictionary mapping member IDs to Member objects.
        _loans (list): List of Loan objects tracking all borrowing events.
    """

    def __init__(self):
        """Initialize an empty Library."""
        self._books = {}
        self._members = {}
        self._loans = []

    @property
    def books(self):
        """Get all books as a dictionary."""
        return self._books.copy()

    @property
    def members(self):
        """Get all members as a dictionary."""
        return self._members.copy()

    @property
    def loans(self):
        """Get all loans as a list."""
        return self._loans.copy()

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): The book to add.

        Raises:
            ValueError: If a book with the same ID already exists.
        """
        if book.id in self._books:
            raise ValueError(f"A book with ID '{book.id}' already exists.")
        self._books[book.id] = book

    def add_member(self, member):
        """
        Add a member to the library.

        Args:
            member (Member): The member to add.

        Raises:
            ValueError: If a member with the same ID already exists.
        """
        if member.member_id in self._members:
            raise ValueError(f"A member with ID '{member.member_id}' already exists.")
        self._members[member.member_id] = member

    def borrow_book(self, member_id, book_id):
        """
        Record a member borrowing a book.

        This method:
        1. Finds the member and book
        2. Checks if the book is available (for physical books)
        3. Checks if the member doesn't already have this book
        4. Decreases available copies (for physical books)
        5. Adds the book to the member's borrowed list
        6. Creates a Loan record

        Args:
            member_id (str): The ID of the member borrowing the book.
            book_id (str): The ID of the book to borrow.

        Raises:
            MemberNotFoundError: If the member doesn't exist.
            BookNotFoundError: If the book doesn't exist.
            BookNotAvailableError: If no copies are available (for physical books).
            InvalidOperationError: If the member already has this book borrowed.
        """
        if member_id not in self._members:
            raise MemberNotFoundError(f"Member with ID '{member_id}' not found.")
        if book_id not in self._books:
            raise BookNotFoundError(f"Book with ID '{book_id}' not found.")

        member = self._members[member_id]
        book = self._books[book_id]

        # Check if member already has this book
        if any(b.id == book_id for b in member.borrowed_books):
            raise InvalidOperationError(
                f"Member {member.name} already has '{book.title}' borrowed."
            )

        # Try to borrow the book
        try:
            book.borrow()
        except Exception as e:
            raise BookNotAvailableError(str(e))

        # Add to member's borrowed list and create loan
        member.borrow_book(book)
        loan = Loan(book, member)
        self._loans.append(loan)

    def return_book(self, member_id, book_id):
        """
        Record a member returning a book.

        This method:
        1. Finds the member and book
        2. Checks if the member has this book borrowed
        3. Increases available copies (for physical books)
        4. Removes the book from the member's borrowed list
        5. Removes the corresponding Loan record

        Args:
            member_id (str): The ID of the member returning the book.
            book_id (str): The ID of the book to return.

        Raises:
            MemberNotFoundError: If the member doesn't exist.
            BookNotFoundError: If the book doesn't exist.
            InvalidOperationError: If the member doesn't have this book borrowed.
        """
        if member_id not in self._members:
            raise MemberNotFoundError(f"Member with ID '{member_id}' not found.")
        if book_id not in self._books:
            raise BookNotFoundError(f"Book with ID '{book_id}' not found.")

        member = self._members[member_id]
        book = self._books[book_id]

        # Check if member has this book
        if not any(b.id == book_id for b in member.borrowed_books):
            raise InvalidOperationError(
                f"Member {member.name} does not have '{book.title}' borrowed."
            )

        # Return the book
        book.return_book()
        member.return_book(book)

        # Remove the loan record
        self._loans = [
            loan for loan in self._loans
            if not (loan.book.id == book_id and loan.member.member_id == member_id)
        ]

    def list_books(self):
        """
        Get a list of all books in the library.

        Returns:
            list: List of Book objects.
        """
        return list(self._books.values())

    def list_members(self):
        """
        Get a list of all members in the library.

        Returns:
            list: List of Member objects.
        """
        return list(self._members.values())

    def get_book_by_id(self, book_id):
        """
        Retrieve a book by its ID.

        Args:
            book_id (str): The book ID.

        Returns:
            Book: The book object, or None if not found.
        """
        return self._books.get(book_id)

    def get_member_by_id(self, member_id):
        """
        Retrieve a member by their ID.

        Args:
            member_id (str): The member ID.

        Returns:
            Member: The member object, or None if not found.
        """
        return self._members.get(member_id)

    def save_to_file(self, filename):
        """
        Save the library state to a JSON file.

        Serializes all books, members, and loans to a JSON file.
        The JSON preserves book types for correct deserialization.

        Args:
            filename (str): Path to the output JSON file.

        Returns:
            None
        """
        data = {
            "books": [book.to_dict() for book in self._books.values()],
            "members": [member.to_dict() for member in self._members.values()],
            "loans": [loan.to_dict() for loan in self._loans],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename):
        """
        Load the library state from a JSON file.

        Deserializes books, members, and loans from a JSON file.
        Reconstructs the in-memory data structures correctly.

        Args:
            filename (str): Path to the input JSON file.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file is not valid JSON.

        Returns:
            None
        """
        with open(filename, "r") as f:
            data = json.load(f)

        # Clear current data
        self._books = {}
        self._members = {}
        self._loans = []

        # Load books
        for book_data in data.get("books", []):
            if book_data["type"] == "PhysicalBook":
                book = PhysicalBook(
                    book_data["id"],
                    book_data["title"],
                    book_data["author"],
                    book_data["available_copies"],
                )
            elif book_data["type"] == "EBook":
                book = EBook(
                    book_data["id"],
                    book_data["title"],
                    book_data["author"],
                    book_data["file_size_mb"],
                )
            self._books[book.id] = book

        # Load members
        for member_data in data.get("members", []):
            member = Member(member_data["member_id"], member_data["name"])
            self._members[member.member_id] = member

        # Load loans and reconstruct relationships
        for loan_data in data.get("loans", []):
            book = self._books.get(loan_data["book_id"])
            member = self._members.get(loan_data["member_id"])
            if book and member:
                loan = Loan(book, member, loan_data["date_borrowed"])
                self._loans.append(loan)
                member.borrow_book(book)

    def __str__(self):
        """Return a readable summary of the library."""
        return (
            f"Library with {len(self._books)} books, "
            f"{len(self._members)} members, "
            f"and {len(self._loans)} active loans"
        )
