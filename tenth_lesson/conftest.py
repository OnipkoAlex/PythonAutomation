import pytest
from .library import Library, Book


@pytest.fixture(scope="session")
def create_library():
    library = Library()
    library.add_book(Book("Harry Potter", "J. K. Rowling"))
    library.add_book(Book("Lord of the Rings", "J. R. R. Tolkien"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("A Tale of Two Cities", "Charles Dickens"))
    library.add_book(Book("The Raven", "Edgar Allan Poe"))
    library.add_book(Book("Treasure Island", "Robert Louis Stevenson"))
    return library
