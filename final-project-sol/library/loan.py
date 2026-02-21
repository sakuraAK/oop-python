"""
Loan module for the Smart Library Management System.

Represents a borrowing event linking a book, member, and date.
"""

from datetime import datetime


class Loan:
    """
    Represents a borrowing event.

    A loan records when a member borrows a book. It requires both a book and a member
    to exist (composition). A loan is created when borrowing succeeds.

    Attributes:
        book (Book): The borrowed book.
        member (Member): The member who borrowed the book.
        date_borrowed (str): The date when the book was borrowed (ISO format).
    """

    def __init__(self, book, member, date_borrowed=None):
        """
        Initialize a Loan instance.

        Args:
            book (Book): The book being borrowed.
            member (Member): The member borrowing the book.
            date_borrowed (str, optional): Date in ISO format. Defaults to today's date.

        Raises:
            ValueError: If book or member is None.
        """
        if book is None or member is None:
            raise ValueError("Loan requires both a book and a member.")
        self.book = book
        self.member = member
        self.date_borrowed = date_borrowed or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        """
        Convert the loan to a dictionary representation.

        Returns:
            dict: Dictionary with book ID, member ID, and date borrowed.
        """
        return {
            "book_id": self.book.id,
            "member_id": self.member.member_id,
            "date_borrowed": self.date_borrowed,
        }

    def __str__(self):
        """Return a readable string representation of the loan."""
        return (
            f"Loan: {self.member.name} borrowed '{self.book.title}' on {self.date_borrowed}"
        )

    def __eq__(self, other):
        """Compare loans by book and member."""
        if not isinstance(other, Loan):
            return False
        return (
            self.book.id == other.book.id
            and self.member.member_id == other.member.member_id
        )
