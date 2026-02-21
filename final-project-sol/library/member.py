"""
Member module for the Smart Library Management System.

Represents a library member and their borrowing history.
"""


class Member:
    """
    Represents a library member.

    A member can borrow books and must manage their borrowed items.
    The same book cannot be borrowed twice simultaneously.

    Attributes:
        _member_id (str): Unique identifier for the member.
        _name (str): Full name of the member.
        _borrowed_books (list): List of books currently borrowed by the member.
    """

    def __init__(self, member_id, name):
        """
        Initialize a Member instance.

        Args:
            member_id (str): Unique identifier for the member.
            name (str): Full name of the member.
        """
        self._member_id = member_id
        self._name = name
        self._borrowed_books = []

    @property
    def member_id(self):
        """Get the member ID."""
        return self._member_id

    @property
    def name(self):
        """Get the member's name."""
        return self._name

    @property
    def borrowed_books(self):
        """Get the list of currently borrowed books."""
        return self._borrowed_books.copy()

    def borrow_book(self, book):
        """
        Borrow a book.

        Args:
            book (Book): The book to borrow.

        Raises:
            ValueError: If the member already has this book borrowed.
        """
        if any(b.id == book.id for b in self._borrowed_books):
            raise ValueError(
                f"Member {self._name} already has '{book.title}' borrowed."
            )
        self._borrowed_books.append(book)

    def return_book(self, book):
        """
        Return a borrowed book.

        Args:
            book (Book): The book to return.

        Raises:
            ValueError: If the member does not have this book borrowed.
        """
        for i, b in enumerate(self._borrowed_books):
            if b.id == book.id:
                self._borrowed_books.pop(i)
                return
        raise ValueError(
            f"Member {self._name} does not have '{book.title}' borrowed."
        )

    def to_dict(self):
        """
        Convert the member to a dictionary representation.

        Returns:
            dict: Dictionary with member ID, name, and list of borrowed book IDs.
        """
        return {
            "member_id": self._member_id,
            "name": self._name,
            "borrowed_books": [book.id for book in self._borrowed_books],
        }

    def __str__(self):
        """Return a readable string representation of the member."""
        return f"{self._name} (ID: {self._member_id}) - {len(self._borrowed_books)} books borrowed"

    def __eq__(self, other):
        """Compare members by their ID."""
        if not isinstance(other, Member):
            return False
        return self._member_id == other._member_id
