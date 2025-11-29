class Book:
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
    
    def get_author(self):
        return self._author
    
    def get_year(self):
        return int(self._year)

    def __str__(self):
        return f"Author: {self._author}; Title: {self._title}; First published: {self._year}"


book1 = Book("Cudjo", "Stephen King", "1981")
book2 = Book("War and Peace", "Leo Tolstoy", "1881")
book3 = Book("Dark Tower 1", "Stephen King", "1981")
book4 = Book("Dark Tower 2", "Stephen King", "1981")
book5 = Book("Dark Tower 3", "Stephen King", "1981")

library = [book1, book2, book3, book4, book5]

def print_all_books(list_of_books):
    for book in list_of_books:
        print(book) 

def get_books_by_author(list_of_books, author):
    filtered_list = []
    for book in list_of_books:
        if book.get_author() == author:
            filtered_list.append(book)
    return filtered_list

def get_oldest(list_of_books: list[Book]):
    minimal_year = 3000
    oldest_book = None
    for book in list_of_books:
        if book.get_year() < minimal_year:
            minimal_year = book.get_year()
            oldest_book = book
    return oldest_book


print("\nPrinting list of books")
print_all_books(library)

print("\nPrinting books written by: Stephen King")
filtered_books = get_books_by_author(library, "Stephen King")
print_all_books(filtered_books)

print("\nPrinting the oldest book")
oldest_book = get_oldest(library)
print(oldest_book)
