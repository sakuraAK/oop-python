"""
Unit tests for the Smart Library Management System.

Tests cover all major functionality including:
- Book creation and operations
- Member management
- Library borrowing and returning
- JSON persistence
- Error handling
"""

import json
import os
import pytest
from library import (
    Library,
    PhysicalBook,
    EBook,
    Member,
    Loan,
    BookNotAvailableError,
    BookNotFoundError,
    MemberNotFoundError,
    InvalidOperationError,
)


@pytest.fixture
def library():
    """Provide an empty library for each test."""
    return Library()


@pytest.fixture
def sample_physical_book():
    """Provide a sample physical book."""
    return PhysicalBook("B001", "Python Programming", "John Doe", 3)


@pytest.fixture
def sample_ebook():
    """Provide a sample e-book."""
    return EBook("E001", "Design Patterns", "Jane Smith", 5.2)


@pytest.fixture
def sample_member():
    """Provide a sample member."""
    return Member("M001", "Alice Johnson")


# ============================================================================
# Book Tests
# ============================================================================


class TestPhysicalBook:
    """Tests for PhysicalBook class."""

    def test_create_physical_book(self, sample_physical_book):
        """Test creating a physical book."""
        assert sample_physical_book.id == "B001"
        assert sample_physical_book.title == "Python Programming"
        assert sample_physical_book.author == "John Doe"
        assert sample_physical_book.available_copies == 3

    def test_borrow_decreases_copies(self, sample_physical_book):
        """Test that borrowing decreases available copies."""
        assert sample_physical_book.available_copies == 3
        sample_physical_book.borrow()
        assert sample_physical_book.available_copies == 2

    def test_return_increases_copies(self, sample_physical_book):
        """Test that returning increases available copies."""
        sample_physical_book.borrow()
        sample_physical_book.return_book()
        assert sample_physical_book.available_copies == 3

    def test_borrow_unavailable_raises_error(self, sample_physical_book):
        """Test that borrowing unavailable book raises error."""
        sample_physical_book._available_copies = 0
        with pytest.raises(Exception):
            sample_physical_book.borrow()

    def test_to_dict(self, sample_physical_book):
        """Test serialization to dictionary."""
        data = sample_physical_book.to_dict()
        assert data["type"] == "PhysicalBook"
        assert data["id"] == "B001"
        assert data["title"] == "Python Programming"
        assert data["available_copies"] == 3

    def test_physical_book_equality(self, sample_physical_book):
        """Test book equality by ID."""
        book2 = PhysicalBook("B001", "Different Title", "Other Author", 1)
        assert sample_physical_book == book2

    def test_physical_book_str(self, sample_physical_book):
        """Test string representation."""
        result = str(sample_physical_book)
        assert "Python Programming" in result
        assert "3 copies available" in result

    def test_negative_copies_raises_error(self):
        """Test that negative copies raises error."""
        with pytest.raises(ValueError):
            PhysicalBook("B001", "Title", "Author", -1)


class TestEBook:
    """Tests for EBook class."""

    def test_create_ebook(self, sample_ebook):
        """Test creating an e-book."""
        assert sample_ebook.id == "E001"
        assert sample_ebook.title == "Design Patterns"
        assert sample_ebook.author == "Jane Smith"
        assert sample_ebook.file_size_mb == 5.2

    def test_ebook_borrow_always_succeeds(self, sample_ebook):
        """Test that e-books can always be borrowed."""
        # E-books should not raise on borrow
        sample_ebook.borrow()
        sample_ebook.borrow()
        # No exception should be raised

    def test_ebook_return_always_succeeds(self, sample_ebook):
        """Test that e-books can always be returned."""
        sample_ebook.return_book()
        # No exception should be raised

    def test_to_dict(self, sample_ebook):
        """Test serialization to dictionary."""
        data = sample_ebook.to_dict()
        assert data["type"] == "EBook"
        assert data["id"] == "E001"
        assert data["file_size_mb"] == 5.2

    def test_ebook_equality(self, sample_ebook):
        """Test e-book equality by ID."""
        book2 = EBook("E001", "Different Title", "Other Author", 10.0)
        assert sample_ebook == book2

    def test_ebook_str(self, sample_ebook):
        """Test string representation."""
        result = str(sample_ebook)
        assert "Design Patterns" in result
        assert "5.2 MB" in result

    def test_negative_file_size_raises_error(self):
        """Test that negative file size raises error."""
        with pytest.raises(ValueError):
            EBook("E001", "Title", "Author", -1.0)


# ============================================================================
# Member Tests
# ============================================================================


class TestMember:
    """Tests for Member class."""

    def test_create_member(self, sample_member):
        """Test creating a member."""
        assert sample_member.member_id == "M001"
        assert sample_member.name == "Alice Johnson"
        assert len(sample_member.borrowed_books) == 0

    def test_borrow_book(self, sample_member, sample_physical_book):
        """Test that member can borrow a book."""
        sample_member.borrow_book(sample_physical_book)
        assert len(sample_member.borrowed_books) == 1
        assert sample_member.borrowed_books[0] == sample_physical_book

    def test_cannot_borrow_same_book_twice(self, sample_member, sample_physical_book):
        """Test that member cannot borrow same book twice."""
        sample_member.borrow_book(sample_physical_book)
        with pytest.raises(ValueError):
            sample_member.borrow_book(sample_physical_book)

    def test_return_book(self, sample_member, sample_physical_book):
        """Test that member can return a book."""
        sample_member.borrow_book(sample_physical_book)
        sample_member.return_book(sample_physical_book)
        assert len(sample_member.borrowed_books) == 0

    def test_cannot_return_unborrrowed_book(self, sample_member, sample_physical_book):
        """Test that member cannot return a book they don't have."""
        with pytest.raises(ValueError):
            sample_member.return_book(sample_physical_book)

    def test_to_dict(self, sample_member, sample_physical_book):
        """Test serialization to dictionary."""
        sample_member.borrow_book(sample_physical_book)
        data = sample_member.to_dict()
        assert data["member_id"] == "M001"
        assert data["name"] == "Alice Johnson"
        assert "B001" in data["borrowed_books"]

    def test_member_equality(self, sample_member):
        """Test member equality by ID."""
        member2 = Member("M001", "Different Name")
        assert sample_member == member2

    def test_member_str(self, sample_member):
        """Test string representation."""
        result = str(sample_member)
        assert "Alice Johnson" in result
        assert "M001" in result


# ============================================================================
# Loan Tests
# ============================================================================


class TestLoan:
    """Tests for Loan class."""

    def test_create_loan(self, sample_physical_book, sample_member):
        """Test creating a loan."""
        loan = Loan(sample_physical_book, sample_member)
        assert loan.book == sample_physical_book
        assert loan.member == sample_member
        assert loan.date_borrowed is not None

    def test_loan_with_custom_date(self, sample_physical_book, sample_member):
        """Test creating a loan with custom date."""
        loan = Loan(sample_physical_book, sample_member, "2026-02-20")
        assert loan.date_borrowed == "2026-02-20"

    def test_loan_requires_book_and_member(self):
        """Test that loan requires both book and member."""
        member = Member("M001", "Alice")
        with pytest.raises(ValueError):
            Loan(None, member)

    def test_loan_to_dict(self, sample_physical_book, sample_member):
        """Test loan serialization."""
        loan = Loan(sample_physical_book, sample_member, "2026-02-20")
        data = loan.to_dict()
        assert data["book_id"] == "B001"
        assert data["member_id"] == "M001"
        assert data["date_borrowed"] == "2026-02-20"

    def test_loan_equality(self, sample_physical_book, sample_member):
        """Test loan equality."""
        loan1 = Loan(sample_physical_book, sample_member)
        loan2 = Loan(sample_physical_book, sample_member)
        assert loan1 == loan2

    def test_loan_str(self, sample_physical_book, sample_member):
        """Test string representation."""
        loan = Loan(sample_physical_book, sample_member, "2026-02-20")
        result = str(loan)
        assert "Alice Johnson" in result
        assert "Python Programming" in result
        assert "2026-02-20" in result


# ============================================================================
# Library Tests
# ============================================================================


class TestLibrary:
    """Tests for Library class."""

    def test_create_empty_library(self, library):
        """Test creating an empty library."""
        assert len(library.books) == 0
        assert len(library.members) == 0
        assert len(library.loans) == 0

    def test_add_book(self, library, sample_physical_book):
        """Test adding a book to the library."""
        library.add_book(sample_physical_book)
        assert len(library.books) == 1
        assert library.get_book_by_id("B001") == sample_physical_book

    def test_cannot_add_duplicate_book(self, library, sample_physical_book):
        """Test that duplicate book IDs are rejected."""
        library.add_book(sample_physical_book)
        with pytest.raises(ValueError):
            library.add_book(sample_physical_book)

    def test_add_member(self, library, sample_member):
        """Test adding a member to the library."""
        library.add_member(sample_member)
        assert len(library.members) == 1
        assert library.get_member_by_id("M001") == sample_member

    def test_cannot_add_duplicate_member(self, library, sample_member):
        """Test that duplicate member IDs are rejected."""
        library.add_member(sample_member)
        with pytest.raises(ValueError):
            library.add_member(sample_member)

    def test_borrow_book_success(self, library, sample_physical_book, sample_member):
        """Test successful book borrowing."""
        library.add_book(sample_physical_book)
        library.add_member(sample_member)
        library.borrow_book("M001", "B001")

        assert len(library.loans) == 1
        assert len(sample_member.borrowed_books) == 1
        assert sample_physical_book.available_copies == 2

    def test_borrow_nonexistent_member(self, library, sample_physical_book):
        """Test borrowing with nonexistent member."""
        library.add_book(sample_physical_book)
        with pytest.raises(MemberNotFoundError):
            library.borrow_book("INVALID", "B001")

    def test_borrow_nonexistent_book(self, library, sample_member):
        """Test borrowing nonexistent book."""
        library.add_member(sample_member)
        with pytest.raises(BookNotFoundError):
            library.borrow_book("M001", "INVALID")

    def test_borrow_unavailable_book(self, library, sample_member):
        """Test borrowing unavailable physical book."""
        book = PhysicalBook("B001", "Title", "Author", 0)
        library.add_book(book)
        library.add_member(sample_member)
        with pytest.raises(BookNotAvailableError):
            library.borrow_book("M001", "B001")

    def test_cannot_borrow_same_book_twice(
        self, library, sample_physical_book, sample_member
    ):
        """Test that member cannot borrow same book twice."""
        library.add_book(sample_physical_book)
        library.add_member(sample_member)
        library.borrow_book("M001", "B001")
        with pytest.raises(InvalidOperationError):
            library.borrow_book("M001", "B001")

    def test_return_book_success(
        self, library, sample_physical_book, sample_member
    ):
        """Test successful book return."""
        library.add_book(sample_physical_book)
        library.add_member(sample_member)
        library.borrow_book("M001", "B001")

        assert sample_physical_book.available_copies == 2
        library.return_book("M001", "B001")
        assert sample_physical_book.available_copies == 3
        assert len(library.loans) == 0

    def test_return_nonexistent_member(self, library, sample_physical_book):
        """Test returning with nonexistent member."""
        library.add_book(sample_physical_book)
        with pytest.raises(MemberNotFoundError):
            library.return_book("INVALID", "B001")

    def test_return_nonexistent_book(self, library, sample_member):
        """Test returning nonexistent book."""
        library.add_member(sample_member)
        with pytest.raises(BookNotFoundError):
            library.return_book("M001", "INVALID")

    def test_cannot_return_unborrrowed_book(
        self, library, sample_physical_book, sample_member
    ):
        """Test returning a book the member doesn't have."""
        library.add_book(sample_physical_book)
        library.add_member(sample_member)
        with pytest.raises(InvalidOperationError):
            library.return_book("M001", "B001")

    def test_list_books(self, library, sample_physical_book, sample_ebook):
        """Test listing all books."""
        library.add_book(sample_physical_book)
        library.add_book(sample_ebook)
        books = library.list_books()
        assert len(books) == 2

    def test_list_members(self, library, sample_member):
        """Test listing all members."""
        library.add_member(sample_member)
        members = library.list_members()
        assert len(members) == 1

    def test_library_str(self, library):
        """Test string representation."""
        result = str(library)
        assert "0 books" in result
        assert "0 members" in result


# ============================================================================
# Persistence Tests
# ============================================================================


class TestPersistence:
    """Tests for JSON persistence."""

    def test_save_to_file(self, library, sample_physical_book, sample_member):
        """Test saving library to JSON file."""
        library.add_book(sample_physical_book)
        library.add_member(sample_member)
        library.borrow_book("M001", "B001")

        filename = "test_library.json"
        library.save_to_file(filename)

        assert os.path.exists(filename)
        with open(filename) as f:
            data = json.load(f)
        assert len(data["books"]) == 1
        assert len(data["members"]) == 1
        assert len(data["loans"]) == 1

        os.remove(filename)

    def test_load_from_file(self, library, sample_physical_book, sample_member):
        """Test loading library from JSON file."""
        library.add_book(sample_physical_book)
        library.add_member(sample_member)
        library.borrow_book("M001", "B001")

        filename = "test_library_load.json"
        library.save_to_file(filename)

        # Create new library and load
        library2 = Library()
        library2.load_from_file(filename)

        assert len(library2.books) == 1
        assert len(library2.members) == 1
        assert len(library2.loans) == 1

        # Verify book type is correct
        book = library2.get_book_by_id("B001")
        assert isinstance(book, PhysicalBook)
        assert book.available_copies == 2

        os.remove(filename)

    def test_load_preserves_ebook_type(self):
        """Test that e-books are preserved correctly in JSON."""
        library = Library()
        ebook = EBook("E001", "Python Guide", "Author", 3.5)
        library.add_book(ebook)

        filename = "test_ebook.json"
        library.save_to_file(filename)

        library2 = Library()
        library2.load_from_file(filename)

        loaded_book = library2.get_book_by_id("E001")
        assert isinstance(loaded_book, EBook)
        assert loaded_book.file_size_mb == 3.5

        os.remove(filename)

    def test_load_restores_member_borrowed_books(self):
        """Test that member's borrowed books are restored correctly."""
        library = Library()
        book = PhysicalBook("B001", "Title", "Author", 2)
        member = Member("M001", "Alice")

        library.add_book(book)
        library.add_member(member)
        library.borrow_book("M001", "B001")

        filename = "test_member_books.json"
        library.save_to_file(filename)

        library2 = Library()
        library2.load_from_file(filename)

        restored_member = library2.get_member_by_id("M001")
        assert len(restored_member.borrowed_books) == 1
        assert restored_member.borrowed_books[0].id == "B001"

        os.remove(filename)
