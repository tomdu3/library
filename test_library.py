import unittest
from library import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        Book.used_ids = []  # Reset used book IDs

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Scribner", 5, "1925-04-10")

    def test_valid_book_creation(self):
        book = Book("1984", "George Orwell", 1949, "Secker & Warburg", 3, "1949-06-08")
        self.assertIsNotNone(book)

    def test_book_id_uniqueness(self):
        book1 = Book("Book 1", "Author 1", 2000, "Publisher 1", 1, "2000-01-01")
        book2 = Book("Book 2", "Author 2", 2001, "Publisher 2", 2, "2001-01-01")
        self.assertNotEqual(book1.book_id, book2.book_id)


if __name__ == "__main__":
    unittest.main()
