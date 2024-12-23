import random
from datetime import datetime

class Book:
    """Represents a book in the library."""

    used_ids = []  # List to store used book_ids, so that they cannot be reused
    
    def __init__(self, title, author, year, publisher, copies, publication_date):
        self.validate_inputs(year, copies, publication_date)  # validate the inputs for number and date 
        self.book_id = self.generate_book_id()  # generate a unique book_id
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.copies = copies
        self.available_copies = copies
        self.publication_date = publication_date
    
    def generate_book_id(self):
        """Generate a unique book_id."""
        book_id = random.randint(1000, 9999)  # generate a book_id as a random 5 digit number
        while book_id in self.used_ids:  # check if the book_id has already been used and regenerates a new one
            book_id = random.randint(1000, 9999)  # generate a new book_id
        self.used_ids.append(book_id)  # add the book_id to the used_ids list, so it can be checked later
        return book_id
        

    def validate_inputs(self, year, copies, publication_date):
        """
        Validates the inputs for the Book instance:
        - year should be a number
        - copies should be a number
        - publication_date should be in the format YYYY-MM-DD
        """
        if not isinstance(year, int):
            raise ValueError(f"'year' should be a number. Provided: {year}")
        if not isinstance(copies, int):
            raise ValueError(f"'copies' should be a number. Provided: {copies}")
        try:
            datetime.strptime(publication_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"'publication_date' should be in the format YYYY-MM-DD. Provided: {publication_date}")

    def set_title(self, title):
        """Set the title of the book."""
        self.title = title

    def get_title(self):
        """Get the title of the book."""
        return self.title

    def set_author(self, author):
        """Set the author of the book."""
        self.author = author

    def get_author(self):
        """Get the author of the book."""
        return self.author

    def set_year(self, year):
        """Set the year of the book."""
        self.year = year

    def get_year(self):
        """Get the year of the book."""
        return self.year

    def set_publisher(self, publisher):
        """Set the publisher of the book."""
        self.publisher = publisher

    def get_publisher(self):
        """Get the publisher of the book."""
        return self.publisher

    def set_copies(self, copies):
        """Set the number of copies of the book."""
        self.copies = copies
        self.available_copies = copies

    def get_copies(self):
        """Get the number of copies of the book."""
        return self.copies

    def get_available_copies(self):
        """Get the number of available copies of the book."""
        return self.available_copies

    def __str__(self):
        """Return a string representation of the Book instance."""
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Publisher: {self.publisher}, Copies: {self.copies}, Available Copies: {self.available_copies}"

# Testing of the Book class

try:
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Scribner", 5, "1925-04-10")
except ValueError as e:
    print(f"Failed to create book: {e}")
# Outputs: Failed to create book: 'year' should be a number. Provided: 1925

try:
    book = Book("1984", "George Orwell", 1949, "Secker & Warburg", 3, "1949-06-08")
    print("Book created successfully!")
except ValueError as e:
    print(f"Failed to create book: {e}")
# Outputs: Book created successfully!

print(book)
print(book.used_ids)

class BookList:
    """Represents a collection of books in the library."""

    def __init__(self):
        self.books = {}  # Dictionary to store book instances. It is empty at the beginning

    def add_book(self, book):
        if book.book_id not in self.books:
            self.books[book.book_id] = book
        else:
            raise ValueError("Book already exists in the collection.")

        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of the Book class.")

    def search_book(self, **kwargs):
        for book in self.books.values():
            if all(getattr(book, key, None) == value for key, value in kwargs.items()):
                return book
        raise ValueError("Book not found.")

    def remove_book(self, id):
        if id in self.books:
            del self.books[id]
        else:
            raise ValueError("Book not found in the collection.")
    @property
    def total_books(self):
        return len(self.books)

    def __str__(self):
        return "No books in the collection" if len(self.books) == 0 else f"BookList: {[(book.title,book.author) for book in self.books.values()]}, Total Books: {self.total_books}"

# Testing of the BookList class

try:
    book_list = BookList()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Scribner", 5, "1925-04-10")
    book_list.add_book(book1)
    book_list.add_book(book1)
    print("Book added successfully!")
except ValueError as e:
    print(f"Failed to add book: {e}")
# Outputs: Failed to add book: Book already exists in the collection.

book2 = Book("1984", "George Orwell", 1949, "Secker & Warburg", 3, "1949-06-08")
book_list.add_book(book2)
print(book_list)
print(book_list.total_books)

try:
    book_list.add_book(book2)
except ValueError as e:
    print(f"Failed to add book: {e}")
# Outputs: Failed to add book: Book already exists in the collection.

print(book_list)
book_list.remove_book(book2.book_id)
print(book_list.total_books)

try:
    book_list.remove_book(9999)
except ValueError as e:
    print(f"Failed to remove book: {e}")
# Outputs: Failed to remove book: Book not found in the collection.

try: 
    book_list.search_book(title="The Great Gatsby")
except ValueError as e:
    print(f"Failed to search book: {e}")
# Outputs: Failed to search book: Book not found.



print(book_list)
print(book_list.total_books)