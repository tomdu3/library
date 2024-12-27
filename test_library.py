import unittest
from library import Book, BookList, User, UserList, Loan


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


class TestBookList(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.book1 = Book("1984", "George Orwell", 1949, "Secker & Warburg", 3, "1949-06-08")
        self.book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Scribner", 5, "1925-04-10")

    def test_add_book(self):
        self.book_list.add_book(self.book1)
        self.assertEqual(self.book_list.total_books, 1)

    def test_add_duplicate_book(self):
        self.book_list.add_book(self.book1)
        with self.assertRaises(ValueError):
            self.book_list.add_book(self.book1)

    def test_remove_book(self):
        self.book_list.add_book(self.book1)
        self.book_list.remove_book(self.book1.book_id)
        self.assertEqual(self.book_list.total_books, 0)

    def test_remove_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.book_list.remove_book(9999)

    def test_search_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.book_list.search_book(title="Nonexistent Book")


class TestUser(unittest.TestCase):
    def setUp(self):
        User.usernames = []  # Reset usernames list

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("jdoe", "John", "Doe", 123, "Main Street", "12345", "invalid_email", "1990-01-01")

    def test_invalid_dob(self):
        with self.assertRaises(ValueError):
            User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "01-01-1990")

    def test_valid_user_creation(self):
        user = User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
        self.assertIsNotNone(user)

    def test_duplicate_username(self):
        User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
        with self.assertRaises(ValueError):
            User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")


class TestUserList(unittest.TestCase):
    def setUp(self):
        User.usernames = []  # Reset usernames list
        self.user_list = UserList()
        self.user1 = User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
        self.user2 = User("johnd", "Jane", "Doe", 456, "High Street", "67890", "jane@me.com", "1995-05-15")

    def test_add_user(self):
        self.user_list.add_user(self.user1)
        self.assertEqual(self.user_list.count_users(), 1)

    def test_add_duplicate_user(self):
        self.user_list.add_user(self.user1)
        with self.assertRaises(ValueError):
            self.user_list.add_user(self.user1)

    def test_remove_user(self):
        self.user_list.add_user(self.user1)
        self.user_list.remove_user("John")
        self.assertEqual(self.user_list.count_users(), 0)

    def test_remove_nonexistent_user(self):
        with self.assertRaises(ValueError):
            self.user_list.remove_user("Nonexistent")


class TestLoan(unittest.TestCase):
    def setUp(self):
        self.loan = Loan()
        self.book1 = Book("1984", "George Orwell", 1949, "Secker & Warburg", 1, "1949-06-08")
        self.book2 = Book("Romeo and Juliet", "William Shakespeare", 1597, "Penguin Classics", 2, "1597-05-16")
        self.user = "jdoe"

    def test_borrow_book(self):
        self.loan.borrow_book(self.user, self.book1)
        self.assertEqual(self.loan.user_books_count(self.user), 1)
        self.assertEqual(self.book1.available_copies, 0)

    def test_borrow_unavailable_book(self):
        self.book1.available_copies = 0
        with self.assertRaises(ValueError):
            self.loan.borrow_book(self.user, self.book1)

    def test_return_book(self):
        self.loan.borrow_book(self.user, self.book1)
        self.loan.return_book(self.user, self.book1)
        self.assertEqual(self.loan.user_books_count(self.user), 0)
        self.assertEqual(self.book1.available_copies, 1)

    def test_return_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.loan.return_book(self.user, self.book1)

    def test_multiple_loans(self):
        self.loan.borrow_book(self.user, self.book1)
        self.loan.borrow_book(self.user, self.book2)
        self.assertEqual(self.loan.user_books_count(self.user), 2)


if __name__ == "__main__":
    unittest.main()
