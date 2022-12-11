import book_pb2


# Singleton class to store books
class BookStore:

    # Dictionary to store books, put some dummy data
    _books = {
        "1234": book_pb2.Book(
            ISBN="1234",
            title="Book 1",
            author="Author 1",
            genre="HISTORY",
            publishing_year=2020,
        ),
        "5678": book_pb2.Book(
            ISBN="5678",
            title="Book 2",
            author="Author 2",
            genre="BIOGRAPHY",
            publishing_year=2020,
        ),
        "9012": book_pb2.Book(
            ISBN="9012",
            title="Book 3",
            author="Author 3",
            genre="SCIENCE_FICTION",
            publishing_year=2020,
        ),
    }

    def __new__(cls):
        """Singleton class to be used as a database connection."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(BookStore, cls).__new__(cls)
        return cls.instance
    
    def create_book(self, book: book_pb2.Book):
        """Create a book in the database.
        
        Returns:
            success: True if book is created successfully, False otherwise
            ISBN: ISBN of the book
            message: Message to be sent to the client
        """
        if book.ISBN in self._books:
            return False, book.ISBN, "Book already exists"
        self._books[book.ISBN] = book
        return True, book.ISBN, "Book created successfully"
    
    def get_book(self, book_isbn: str):
        """Get a book from the database.
        
        Returns:
            success: True if book is found, False otherwise
            book: Book object if found, None otherwise
            message: Message to be sent to the client
        """
        if book_isbn not in self._books:
            return False, None, "Book not found"
        return True, self._books[book_isbn], "Book found successfully"


if __name__ == "__main__":
    # Test the BookStore class
    book_store = BookStore()
    book = book_pb2.Book(
        ISBN="1234",
        title="Book 1",
        author="Author 1",
        genre="HISTORY",
        publishing_year=2020,
    )
    print(book_store.create_book(book))
    print(book_store.get_book("1234"))
    print(book_store.get_book("1"))
