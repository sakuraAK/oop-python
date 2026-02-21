"""
Book module for the Smart Library Management System.

Defines abstract base class Book and concrete implementations (PhysicalBook, EBook).
"""

from abc import ABC, abstractmethod


class Book(ABC):
    """
    Abstract base class representing a generic book in the library.

    This class defines the common interface for all book types.
    Subclasses must implement borrow() and return_book() methods.

    Attributes:
        _id (str): Unique identifier for the book.
        _title (str): Title of the book.
        _author (str): Author of the book.
    """

    def __init__(self, book_id, title, author):
        """
        Initialize a Book instance.

        Args:
            book_id (str): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
        """
        self._id = book_id
        self._title = title
        self._author = author

    @property
    def id(self):
        """Get the book ID."""
        return self._id

    @property
    def title(self):
        """Get the book title."""
        return self._title

    @property
    def author(self):
        """Get the book author."""
        return self._author

    @abstractmethod
    def borrow(self):
        """
        Mark the book as borrowed.

        Subclasses must implement this method to handle their specific borrowing logic.
        """
        pass

    @abstractmethod
    def return_book(self):
        """
        Mark the book as returned.

        Subclasses must implement this method to handle their specific return logic.
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Convert the book to a dictionary representation.

        Returns:
            dict: Dictionary containing book data for JSON serialization.
        """
        pass

    def __str__(self):
        """Return a readable string representation of the book."""
        return f"{self._title} by {self._author} (ID: {self._id})"

    def __eq__(self, other):
        """Compare books by their ID."""
        if not isinstance(other, Book):
            return False
        return self._id == other._id


class PhysicalBook(Book):
    """
    Represents a physical book in the library.

    A physical book has a limited number of copies that can be borrowed.

    Attributes:
        _id (str): Unique identifier for the book.
        _title (str): Title of the book.
        _author (str): Author of the book.
        _available_copies (int): Number of available copies.
    """

    def __init__(self, book_id, title, author, available_copies):
        """
        Initialize a PhysicalBook instance.

        Args:
            book_id (str): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
            available_copies (int): Initial number of available copies.

        Raises:
            ValueError: If available_copies is negative.
        """
        super().__init__(book_id, title, author)
        if available_copies < 0:
            raise ValueError("Available copies cannot be negative.")
        self._available_copies = available_copies

    @property
    def available_copies(self):
        """Get the number of available copies."""
        return self._available_copies

    def borrow(self):
        """
        Decrease the number of available copies by 1.

        Raises:
            Exception: If no copies are available.
        """
        if self._available_copies <= 0:
            raise Exception(f"No copies of '{self._title}' are available.")
        self._available_copies -= 1

    def return_book(self):
        """Increase the number of available copies by 1."""
        self._available_copies += 1

    def to_dict(self):
        """
        Convert the physical book to a dictionary.

        Returns:
            dict: Dictionary with book type, ID, title, author, and available copies.
        """
        return {
            "type": "PhysicalBook",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "available_copies": self._available_copies,
        }

    def __str__(self):
        """Return a readable string representation including copy count."""
        return (
            f"{self._title} by {self._author} (ID: {self._id}) "
            f"- {self._available_copies} copies available"
        )


class EBook(Book):
    """
    Represents an e-book in the library.

    An e-book can be borrowed by unlimited members simultaneously (it has unlimited copies).

    Attributes:
        _id (str): Unique identifier for the book.
        _title (str): Title of the book.
        _author (str): Author of the book.
        _file_size_mb (float): Size of the e-book file in megabytes.
    """

    def __init__(self, book_id, title, author, file_size_mb):
        """
        Initialize an EBook instance.

        Args:
            book_id (str): Unique identifier for the book.
            title (str): Title of the book.
            author (str): Author of the book.
            file_size_mb (float): Size of the e-book file in megabytes.

        Raises:
            ValueError: If file_size_mb is negative.
        """
        super().__init__(book_id, title, author)
        if file_size_mb < 0:
            raise ValueError("File size cannot be negative.")
        self._file_size_mb = file_size_mb

    @property
    def file_size_mb(self):
        """Get the file size in megabytes."""
        return self._file_size_mb

    def borrow(self):
        """
        Borrow an e-book.

        E-books have unlimited copies, so this method always succeeds.
        """
        pass

    def return_book(self):
        """
        Return an e-book.

        E-books have unlimited copies, so this method always succeeds.
        """
        pass

    def to_dict(self):
        """
        Convert the e-book to a dictionary.

        Returns:
            dict: Dictionary with book type, ID, title, author, and file size.
        """
        return {
            "type": "EBook",
            "id": self._id,
            "title": self._title,
            "author": self._author,
            "file_size_mb": self._file_size_mb,
        }

    def __str__(self):
        """Return a readable string representation including file size."""
        return (
            f"{self._title} by {self._author} (ID: {self._id}) "
            f"- {self._file_size_mb} MB"
        )
