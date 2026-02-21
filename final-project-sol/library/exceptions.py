"""
Custom exceptions for the Smart Library Management System.

Provides domain-specific exceptions for library operations.
"""


class BookNotAvailableError(Exception):
    """Raised when a book cannot be borrowed because no copies are available."""
    pass


class BookNotFoundError(Exception):
    """Raised when a book with the given ID is not found in the library."""
    pass


class MemberNotFoundError(Exception):
    """Raised when a member with the given ID is not found in the library."""
    pass


class InvalidOperationError(Exception):
    """Raised when an invalid operation is attempted (e.g., returning a book not borrowed)."""
    pass
