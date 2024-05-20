from .library import Book


def test_creating_library(create_library):
    """"Checking if creating library works"""
    assert len(create_library.books) == 6


def test_adding_book(create_library):
    """"Checking if the book was added"""
    book = Book("Bible", "Unknown")
    create_library.add_book(book)
    assert any(book in create_library.books for book in create_library.books) is True


def test_finding_book_by_title(create_library):
    """"Checking if search works"""
    assert create_library.find_book_by_title("Harry Potter") is not None


def test_removing_book_by_title(create_library):
    """"Checking if removing book works"""
    book = Book("The Never-ending Story", "Michael Ende")
    create_library.add_book(book)
    create_library.remove_book(book)
    assert create_library.find_book_by_title("The Never-ending Story") is None
