import random
import sys
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
        return f"id: {self.book_id}, Book: {self.title}, Author: {self.author}, Year: {self.year}, Publisher: {self.publisher}, Copies: {self.copies}, Available Copies: {self.available_copies}"

#############################
# Testing of the Book class #
#############################

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

################################
# End of testing of Book class #
################################

class BookList:
    """Represents a collection of books in the library."""

    def __init__(self):
        """
        Constructor for the BookList class.
        It initializes an empty dictionary to store book instances.
        """
        self.books = {}  # Dictionary to store book instances. It is empty at the beginning

    def add_book(self, book):
        """Add a book to the collection."""
        if book.book_id not in self.books:  # check if the book has already been added 
            self.books[book.book_id] = book  # add the book to the dictionary
            print(f"Book '{book.title}' by {book.author} added successfully!")
        else:
            print("Book not added.")
            raise ValueError("Book already exists in the collection.")

        if not isinstance(book, Book):  # check if the book is an instance of the Book class
            print("Book not added.")
            raise ValueError("Book must be an instance of the Book class.")

    def search_book(self, **kwargs):
        """Search for a book in the collection by keyword arguments."""
        for book in self.books.values():
            if all(getattr(book, key, None) == value for key, value in kwargs.items()):
                return book
        raise ValueError("Book not found.")

    def remove_book(self, id):
        """Remove a book from the collection by its ID."""
        if id in self.books:
            del self.books[id]
        else:
            raise ValueError("Book not found in the collection.")

    @property  # decorator that makes the method total_books a property, so that it can be accessed like an attribute
    def total_books(self):
        """Return the total number of books in the collection."""
        return len(self.books)

    def __str__(self):
        return "No books in the collection" if len(self.books) == 0 else f"BookList: {[(book.title,book.author) for book in self.books.values()]}, Total Books: {self.total_books}"

#################################
# Testing of the BookList class #
#################################

try:
    book_list = BookList()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Scribner", 5, "1925-04-10")
    book_list.add_book(book1)
    book_list.add_book(book1)
    print("Book added successfully!")
except ValueError as e:
    print(f"Failed to add book: {e}")
# Outputs: Failed to add book: Book already exists in the collection.

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Scribner", 5, "1925-04-10")
book_list.add_book(book1)
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
# book_list.search_book(title="The Great Gatsby")

book_list.remove_book(book2.book_id)
print(book_list.total_books)


try:
    book_list.remove_book(9999)
except ValueError as e:
    print(f"Failed to remove book: {e}")
# Outputs: Failed to remove book: Book not found in the collection.

book_list.remove_book(book1.book_id)
try: 
    book_list.search_book(title="The Great Gatsby")
except ValueError as e:
    print(f"Failed to search book: {e}")
# Outputs: Failed to search book: Book not found.



print(book_list)
print(book_list.total_books)

####################################
# End of testing of BookList class #
####################################

class User:
    """Represents a user of the library."""

    usernames = []  # List to store existing usernames

    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, dob):
        self.check_username(username)
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.validate_email(email)
        self.email = email
        self.validate_dob(dob)
        self.dob = dob
        User.usernames.append(username)


    def check_username(self, username):
        if username in User.usernames:  # check if the username already exists on the list
            raise ValueError("Username already exists")

    def get_username(self):
        """Returns the username of the user."""
        return self.username

    def get_firstname(self):
        """Returns the first name of the user."""
        return self.firstname

    def set_firstname(self, firstname):
        """Sets the first name of the user."""
        self.firstname = firstname

    def get_lastname(self):
        """Returns the last name of the user."""
        return self.surname

    def set_lastname(self, surname):
        """Sets the last name of the user."""
        self.surname = surname

    def get_address(self):
        """Returns the address of the user."""
        return f"{self.house_number} {self.street_name}, {self.postcode}"

    def set_address(self, house_number, street_name, postcode):
        """Sets the address of the user."""
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode

    def validate_email(self, email):
        if "@" not in email or "." not in email:  # this is not a perfect validator, but it's enough for this example
            raise ValueError("Invalid email address")
    
    def get_email(self):
        """Returns the email address of the user."""
        return self.email
    
    def set_email(self, email):
        """Sets the email address of the user."""
        self.email = email
    
    def validate_dob(self, dob):
        try:
            datetime.strptime(dob, "%Y-%m-%d")  # a valid date is in the format YYYY-MM-DD
        except ValueError:
            raise ValueError("Invalid date of birth")

    def get_dob(self):
        """Returns the date of birth of the user."""
        return self.dob
    
    def set_dob(self, dob):
        """Sets the date of birth of the user."""
        self.dob = dob

    def __str__(self):
        return f"User: {self.username}, First Name: {self.firstname}, Last Name: {self.surname}, Address: {self.get_address()}, Email: {self.email}, Date of Birth: {self.dob}"

#############################
# Testing of the User class #
#############################

try:
    user = User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
    print(user)
except ValueError as e:
    print(f"Failed to create user: {e}")
# Outputs: Failed to create user: Username already exists

try:
    user = User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
    print(user)
except ValueError as e:
    print(f"Failed to create user: {e}")
# Outputs: Failed to create user: Invalid email address

try:
    user = User("jdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
    print(user)
except ValueError as e:
    print(f"Failed to create user: {e}")
# Outputs: Failed to create user: Invalid date of birth

print(user.usernames)
user1 = User("jhdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
print(user1)

user2 = User("jodoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
user2.set_firstname("Jane")
print(user2)

user3 = User("johdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
user3.set_lastname("Doe")
print(user3)

user4 = User("johndoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
user4.set_address(456, "Main Street", "12345")
print(user4)

user5 = User("jjdoe", "John", "Doe", 123, "Main Street", "12345", "jdoe@me.com", "1990-01-01")
user5.set_email("jdoe@me.com")
print(user5)

print(user5.usernames)

################################
# End of testing of User class #
################################


class UserList:
    """Represents a collection of users."""

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user
        else:
            raise ValueError("User already exists.")

    def remove_user(self, firstname):
        matches = [user for user in self.users.values() if user.firstname == firstname]
        if len(matches) == 1:
            del self.users[matches[0].username]
        elif len(matches) > 1:
            for user in matches:
                print(user)
            raise ValueError("Multiple users found with this first name.")
        else:
            raise ValueError("User not found.")

    def count_users(self):
        return len(self.users)
    
    def __str__(self):
        return f"UserList: {[(user.username, user.firstname) for user in self.users.values()]}, Total Users: {self.count_users()}"

#################################
# Testing of the UserList class #
#################################

user_list = UserList()

try:
    # add user, user1, user2, user3, user4, user5
    user_list.add_user(user1)
    user_list.add_user(user2)
    user_list.add_user(user3)
    user_list.add_user(user4)
    user_list.add_user(user5)
    print(user_list)
except ValueError as e:
    print(f"Failed to add user: {e}")
# Outputs: Failed to add user: User already exists.

try:
    user_list.remove_user("John")
except ValueError as e:
    print(f"Failed to remove user: {e}")
# Outputs: Failed to remove user: User not found.

print(user_list)
print(user_list.count_users())

####################################
# End of testing of UserList class #
####################################


class Loan:
    """Represents loans of books to users."""

    def __init__(self):
        self.loans = {}  # dictionary to store loans

    def borrow_book(self, username, book):
        if book.available_copies > 0:  # check if the book is available
            book.available_copies -= 1
            if username not in self.loans:  # check if the user has borrowed any books
                self.loans[username] = []  # create a new list for the user
            self.loans[username].append(book)  # add the book to the user's list
        else:
            raise ValueError("No available copies.")

    def return_book(self, username, book):
        """Returns a book borrowed by a user."""
        if username in self.loans and book in self.loans[username]:  # check if the book is borrowed by the user
            book.available_copies += 1
            self.loans[username].remove(book)
        else:
            raise ValueError("Book not borrowed by user.")

    def user_books_count(self, username):
        """Returns the number of books borrowed by a user."""
        return len(self.loans.get(username, []))  # default to an empty list if user not found

    def __str__(self):
        return f"Loan: {[(username, [book.title for book in books]) for username, books in self.loans.items()]}"

##############################
# Testing of the Loan class  #
##############################

loan = Loan()
try:
    loan.borrow_book("jdoe", book1)
except ValueError as e:
    print(f"Failed to borrow book: {e}")
# Outputs: Failed to borrow book: No available copies.

try:
    loan.return_book("jdoe", book1)
except ValueError as e:
    print(f"Failed to return book: {e}")
# Outputs: Failed to return book: Book not borrowed by user.

book3 = Book("Romeo and Juliet", "William Shakespeare", 2012, "Penguin Classics", 5, "1597-05-16")
# loan.borrow_book("jdoe", book1)
loan.borrow_book("jdoe", book2)
loan.borrow_book("jdoe", book3)

try:
    loan.return_book("jdoe", book1)
except ValueError as e:
    print(f"Failed to return book: {e}")
# Outputs: Failed to return book: Book not borrowed by user.

try:
    book1.available_copies = 0
    loan.borrow_book("jdoe", book1)
except ValueError as e:
    print(f"Failed to borrow book: {e}")
# Outputs: Failed to borrow book: No available copies.

print(loan.user_books_count("jdoe"))
print(loan)

################################
# End of testing of Loan Class #
################################

# TODO: Make a dashboard of a library


class LibraryDashboard:
    """Dashboard for managing the library system."""
    
    def __init__(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loan = Loan()

    def display_menu(self):
        """Display the main menu."""
        print("\nLibrary Management System Dashboard")
        print("1. Manage Books")
        print("2. Manage Users")
        print("3. Manage Loans")
        print("4. Exit")

    def manage_books(self):
        """Menu for managing books."""
        while True:
            print("\nManage Books")
            print("1. Add Book")
            print("2. Search Book")
            print("3. Remove Book")
            print("4. View All Books")
            print("5. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.search_book()
            elif choice == "3":
                self.remove_book()
            elif choice == "4":
                self.view_all_books()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_users(self):
        """Menu for managing users."""
        while True:
            print("\nManage Users")
            print("1. Add User")
            print("2. Remove User")
            print("3. View All Users")
            print("4. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.remove_user()
            elif choice == "3":
                self.view_all_users()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_loans(self):
        """Menu for managing loans."""
        while True:
            print("\nManage Loans")
            print("1. Borrow Book")
            print("2. Return Book")
            print("3. View User Loans")
            print("4. View All Books")
            print("5. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.borrow_book()
            elif choice == "2":
                self.return_book()
            elif choice == "3":
                self.view_user_loans()
            elif choice == "4":
                self.view_all_books()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    # Book Management Functions
    def add_book(self):
        """Add a new book to the library."""
        try:
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter year: "))
            publisher = input("Enter publisher: ")
            copies = int(input("Enter number of copies: "))
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            book = Book(title, author, year, publisher, copies, publication_date)
            self.book_list.add_book(book)
        except ValueError as e:
            print(f"Error: {e}")

    def search_book(self):
        """Search for a book."""
        try:
            print("Search by: title, author, publisher, or publication_date")
            key = input("Enter field name: ")
            value = input("Enter value to search: ")
            book = self.book_list.search_book(**{key: value})
            print(book)
        except ValueError as e:
            print(f"Error: {e}")

    def remove_book(self):
        """Remove a book from the library."""
        try:
            title = input("Enter title of the book to remove: ")
            self.book_list.remove_book(title)
        except ValueError as e:
            print(f"Error: {e}")

    def view_all_books(self):
        """View all books in the library."""
        print(self.book_list)

    # User Management Functions
    def add_user(self):
        """Add a new user to the library."""
        try:
            username = input("Enter username: ")
            firstname = input("Enter first name: ")
            surname = input("Enter last name: ")
            house_number = input("Enter house number: ")
            street_name = input("Enter street name: ")
            postcode = input("Enter postcode: ")
            email = input("Enter email: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            user = User(username, firstname, surname, house_number, street_name, postcode, email, dob)
            self.user_list.add_user(user)
        except ValueError as e:
            print(f"Error: {e}")

    def remove_user(self):
        """Remove a user from the library."""
        try:
            firstname = input("Enter first name of the user to remove: ")
            self.user_list.remove_user(firstname)
        except ValueError as e:
            print(f"Error: {e}")

    def view_all_users(self):
        """View all users."""
        print(self.user_list)

    # Loan Management Functions
    def borrow_book(self):
        """Borrow a book."""
        try:
            username = input("Enter username: ")
            book_id = int(input("Enter book ID: "))
            book = self.book_list.books.get(book_id)
            if not book:
                raise ValueError("Book not found.")
            self.loan.borrow_book(username, book)
            print(f"Book '{book.title}' borrowed by {username}.")
        except ValueError as e:
            print(f"Error: {e}")

    def return_book(self):
        """Return a book."""
        try:
            username = input("Enter username: ")
            book_id = int(input("Enter book ID: "))
            book = self.book_list.books.get(book_id)
            if not book:
                raise ValueError("Book not found.")
            self.loan.return_book(username, book)
            print(f"Book '{book.title}' returned by {username}.")
        except ValueError as e:
            print(f"Error: {e}")

    def view_user_loans(self):
        """View books borrowed by a user."""
        username = input("Enter username: ")
        user_loans = self.loan.loans.get(username, [])
        if user_loans:
            print(f"Books borrowed by {username}: {[book.title for book in user_loans]}")
        else:
            print(f"No books borrowed by {username}.")

    # Run Dashboard
    def run(self):
        """Run the dashboard."""
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.manage_books()
            elif choice == "2":
                self.manage_users()
            elif choice == "3":
                self.manage_loans()
            elif choice == "4":
                print("Exiting the system. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

# Initialize and run the dashboard
dashboard = LibraryDashboard()
dashboard.run()


