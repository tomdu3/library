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

