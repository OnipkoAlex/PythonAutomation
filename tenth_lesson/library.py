class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'The book title is {self.title} and the author is {self.author}'

    def __repr__(self):
        return f'Book(\'{self.title}\', \'{self.author}\')'


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def remove_book(self, book: Book):
        self.books.remove(book)
