class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        '''Mark the book as checked out if available.'''
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        '''Mark the book as available again.'''
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        '''Check if the book is not checked out.'''
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        '''Add a Book instance to the library.'''
        self._books.append(book)

    def check_out_book(self, title):
        '''Check out a book by title if available.'''
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        '''Return a checked-out book by title.'''
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        '''Print all books that are currently available.'''
        available_books = [
            book for book in self._books if book.is_available()
        ]
        if not available_books:
            print("No available books.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
