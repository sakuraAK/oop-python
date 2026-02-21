"""
Smart Library Management System - Console Menu Interface.

A simple text-based menu for interacting with the library system.
"""

from library import (
    Library,
    PhysicalBook,
    EBook,
    Member,
    BookNotAvailableError,
    BookNotFoundError,
    MemberNotFoundError,
    InvalidOperationError,
)


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_menu():
    """Display the main menu options."""
    print("\n" + "-" * 60)
    print("MAIN MENU")
    print("-" * 60)
    print("1.  Add Physical Book")
    print("2.  Add E-Book")
    print("3.  Add Member")
    print("4.  Borrow Book")
    print("5.  Return Book")
    print("6.  List All Books")
    print("7.  List All Members")
    print("8.  List Member's Borrowed Books")
    print("9.  Save Library to File")
    print("10. Load Library from File")
    print("11. Exit")
    print("-" * 60)


def add_physical_book(library):
    """Add a physical book to the library."""
    print_header("ADD PHYSICAL BOOK")
    try:
        book_id = input("Enter book ID: ").strip()
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        copies = int(input("Enter number of available copies: ").strip())

        book = PhysicalBook(book_id, title, author, copies)
        library.add_book(book)
        print(f"✓ Successfully added: {book}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def add_ebook(library):
    """Add an e-book to the library."""
    print_header("ADD E-BOOK")
    try:
        book_id = input("Enter book ID: ").strip()
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        file_size = float(input("Enter file size (MB): ").strip())

        book = EBook(book_id, title, author, file_size)
        library.add_book(book)
        print(f"✓ Successfully added: {book}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def add_member(library):
    """Add a member to the library."""
    print_header("ADD MEMBER")
    try:
        member_id = input("Enter member ID: ").strip()
        name = input("Enter member name: ").strip()

        member = Member(member_id, name)
        library.add_member(member)
        print(f"✓ Successfully added: {member}")
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def borrow_book(library):
    """Process a book borrowing transaction."""
    print_header("BORROW BOOK")
    try:
        member_id = input("Enter member ID: ").strip()
        book_id = input("Enter book ID: ").strip()

        library.borrow_book(member_id, book_id)
        print(f"✓ Successfully borrowed book!")
    except MemberNotFoundError as e:
        print(f"✗ Error: {e}")
    except BookNotFoundError as e:
        print(f"✗ Error: {e}")
    except BookNotAvailableError as e:
        print(f"✗ Error: {e}")
    except InvalidOperationError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def return_book(library):
    """Process a book return transaction."""
    print_header("RETURN BOOK")
    try:
        member_id = input("Enter member ID: ").strip()
        book_id = input("Enter book ID: ").strip()

        library.return_book(member_id, book_id)
        print(f"✓ Successfully returned book!")
    except MemberNotFoundError as e:
        print(f"✗ Error: {e}")
    except BookNotFoundError as e:
        print(f"✗ Error: {e}")
    except InvalidOperationError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")


def list_books(library):
    """Display all books in the library."""
    print_header("ALL BOOKS IN LIBRARY")
    books = library.list_books()
    if not books:
        print("No books in the library.")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")


def list_members(library):
    """Display all members in the library."""
    print_header("ALL MEMBERS")
    members = library.list_members()
    if not members:
        print("No members registered.")
    else:
        for i, member in enumerate(members, 1):
            print(f"{i}. {member}")


def list_member_books(library):
    """Display books borrowed by a specific member."""
    print_header("MEMBER'S BORROWED BOOKS")
    try:
        member_id = input("Enter member ID: ").strip()
        member = library.get_member_by_id(member_id)
        if not member:
            print(f"✗ Member with ID '{member_id}' not found.")
            return

        borrowed = member.borrowed_books
        if not borrowed:
            print(f"{member.name} has no borrowed books.")
        else:
            print(f"\nBooks borrowed by {member.name}:")
            for i, book in enumerate(borrowed, 1):
                print(f"{i}. {book}")
    except Exception as e:
        print(f"✗ Error: {e}")


def save_library(library):
    """Save library data to a JSON file."""
    print_header("SAVE LIBRARY")
    try:
        filename = input("Enter filename (default: data.json): ").strip()
        if not filename:
            filename = "data.json"
        library.save_to_file(filename)
        print(f"✓ Library saved to {filename}")
    except Exception as e:
        print(f"✗ Error: {e}")


def load_library(library):
    """Load library data from a JSON file."""
    print_header("LOAD LIBRARY")
    try:
        filename = input("Enter filename (default: data.json): ").strip()
        if not filename:
            filename = "data.json"
        library.load_from_file(filename)
        print(f"✓ Library loaded from {filename}")
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found.")
    except Exception as e:
        print(f"✗ Error: {e}")


def main():
    """Main program loop."""
    library = Library()
    print_header("SMART LIBRARY MANAGEMENT SYSTEM")
    print("Welcome! Type your choice to begin.\n")

    while True:
        print_menu()
        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_physical_book(library)
        elif choice == "2":
            add_ebook(library)
        elif choice == "3":
            add_member(library)
        elif choice == "4":
            borrow_book(library)
        elif choice == "5":
            return_book(library)
        elif choice == "6":
            list_books(library)
        elif choice == "7":
            list_members(library)
        elif choice == "8":
            list_member_books(library)
        elif choice == "9":
            save_library(library)
        elif choice == "10":
            load_library(library)
        elif choice == "11":
            print("\n" + "=" * 60)
            print("  Thank you for using the Library Management System!")
            print("=" * 60 + "\n")
            break
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 11.")


if __name__ == "__main__":
    main()
