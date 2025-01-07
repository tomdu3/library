# Library Management System

[Link to the Repository](https://github.com/tomdu3/library)

## Table of Contents

<!-- TOC -->

- [Library Management System](#library-management-system)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
    - [Task 1:](#task-1)
      - [Class - Books:](#class---books)
      - [Class - BookList:](#class---booklist)
      - [Class - Users:](#class---users)
      - [Class - UserList:](#class---userlist)
      - [Class - Loans:](#class---loans)
    - [Other features:](#other-features)
    - [Task 2](#task-2)
      - [Create a Class diagram:](#create-a-class-diagram)
    - [Task 3](#task-3)
  - [Testing](#testing)
  - [UML Diagram](#uml-diagram)

<!-- /TOC -->

## Project Description

The project consists of 3 tasks:

1. Create a python library record system.
2. Create a UML class diagram for the software modelling.
3. Create a training document or presentation to explain the code and functionality of the software. So that i can learn how it all works.

More detail of the task:

### Task 1:

Create a library record system in Python using object oriented programming concepts. It should be possible to create objects from your implemented Python classes. Each class should contain information about different parts of the system. The objects should be created from the classes and interact with each other to achieve the correct functionality of the system. There are several Python classes to be written. The system should include the following Python classes as minimum: Books, BookList, Users, UserList and Loans. See the Tasks below for specific details about each class.

#### Class - Books:

Define a Python class with methods to do the following:

1. Define a constructor to create new book records. Each record should have include the following attributes:

- Randomly generated book ID, title, author, year, publisher, number of available copies and publication date.

2. Define different methods to set each of the following book attributes, one method per attribute:

- title, author, year, publisher, number of available copies and publication date.

3. Different methods to return each the following book attribute, one method per attribute:

- title, author, year, publisher, number of copies, available number of copies and publication attribute.

4. The class should include error checking (e.g., exception handling).
5. The class should be heavily documented by comments.

#### Class - BookList:

Define a Python class with methods to do the following:

1. A constructor to create new object from this class.
2. A method to store a collection (e.g., dictionary). The collection should store book instances that are created from the Book object.
3. A method to search through the collection and find a book by one of the following data:

- title, author, publisher OR publication date.

4. A method to remove a book from the collection. The book should be specified by its title.
5. A method to return the total number of books stored in the collection.
6. The class should include error checking (e.g., exception handling).
7. The class should be heavily documented by comments.

#### Class - Users:

Define a Python class with functions to do the following:

1. A constructor to create a user with the following attributes:

- username, firstname, surname, house number, street name, postcode, email address, and date of birth.

2. A method to return the following attributes:

- username, firstname, surname, house number, street name, postcode, email address, and date of birth. You should have one method per attribute.

3. Different methods to edit the following attribute:

- firstname, surname, email address, and date of birth. You should have one method per attribute.

4. The class should include appropriate error checking.
5. The class should have be well documented by comments.

#### Class - UserList:

Define a Python class with functions to do the following:

1. A constructor to create new object from this class.
2. A method to store a collection (e.g., dictionary) of user instances that are created with the class Users.
3. A method to remove a user from the collection by giving the user’s first name. This operation must inform program users if there are two or more users with same first name.
4. A method to count the number of users in the system. This should be based on the number of user object in the collection.
5. A method to return a user’s detail by the username.
6. The class should include appropriate error checking (e.g., exception handling).
7. The class should be well documented by comments.

#### Class - Loans:

Define a Python class with methods to do the following:

1. A constructor to create new object from this class.
2. A method for a user to borrow a book. This method should have appropriate features to assign a book to a user. The information could be stored in an appropriate data structure for further processing.
3. A method for a user to return a book. This method should un-assign a book previously assigned to a user.
4. A method to count and return the total number of books a user is currently borrowing.
5. A method to print out all the overdue books along with the users’ username and first name. The username and first name of the user should be retrieved through the appropriate methods in the User class.
6. The class should include appropriate error checking (e.g., exception handling).
7. The class should be well documented by comments.

### Other features:

The following features should also be included:

1. Books: Modify a book’s title, author, year, and publisher and number of copies from an easy to use command line user interface.
2. Users: Modify a user’s first name, surname, house number, street name, postcode from an easy to use command line user interface.

### Task 2

#### Create a Class diagram:

Create a UML class diagram for the software modelling. The UML diagram should contain the full system design and should reflect your system implementation.

1. The UML diagram should include all the properties of the classes, the correct methods and the correct association between the classes. The diagram should reflect the system and class implementations.

### Task 3

Prepare a document or recorded presentation of all the features and functionalities of the software. Your presentation should show at least the following aspects of the system:

- Clear view of the user interface.
- Clear view of the source code generating the user interface.
- Clear view of the source code of different classes you have implemented.
- Show all the system functionalities using different types of input and the way your system handles errors and potential problems.

## Testing

The project tests are written in pytest and placed in `test_library.py`. For tests to be run, pytest must be installed.

`pip install pytest`

To run the tests, execute the following command in the project directory:

`pytest` or `pytest --verbose`

This is the output of the tests:

```bash
============================= test session starts ==============================
platform linux -- Python 3.12.7, pytest-7.4.4, pluggy-1.0.0 -- /home/tom/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /home/tom/upwork/terry/library
plugins: anyio-4.2.0
collecting ... collected 21 items

test_library.py::TestBook::test_book_id_uniqueness PASSED                [  4%]
test_library.py::TestBook::test_invalid_year PASSED                      [  9%]
test_library.py::TestBook::test_valid_book_creation PASSED               [ 14%]
test_library.py::TestBookList::test_add_book PASSED                      [ 19%]
test_library.py::TestBookList::test_add_duplicate_book PASSED            [ 23%]
test_library.py::TestBookList::test_remove_book PASSED                   [ 28%]
test_library.py::TestBookList::test_remove_nonexistent_book PASSED       [ 33%]
test_library.py::TestBookList::test_search_nonexistent_book PASSED       [ 38%]
test_library.py::TestUser::test_duplicate_username PASSED                [ 42%]
test_library.py::TestUser::test_invalid_dob PASSED                       [ 47%]
test_library.py::TestUser::test_invalid_email PASSED                     [ 52%]
test_library.py::TestUser::test_valid_user_creation PASSED               [ 57%]
test_library.py::TestUserList::test_add_duplicate_user PASSED            [ 61%]
test_library.py::TestUserList::test_add_user PASSED                      [ 66%]
test_library.py::TestUserList::test_remove_nonexistent_user PASSED       [ 71%]
test_library.py::TestUserList::test_remove_user PASSED                   [ 76%]
test_library.py::TestLoan::test_borrow_book PASSED                       [ 80%]
test_library.py::TestLoan::test_borrow_unavailable_book PASSED           [ 85%]
test_library.py::TestLoan::test_multiple_loans PASSED                    [ 90%]
test_library.py::TestLoan::test_return_book PASSED                       [ 95%]
test_library.py::TestLoan::test_return_nonexistent_book PASSED           [100%]

============================== 21 passed in 0.02s ==============================
```

## UML Diagram

UML Diagram was made in [MarkDown](https://www.markdownguide.org/) tables and [Mermaid](https://mermaid-js.github.io/mermaid/#/) diagrams.

- [Link to the UML Diagram](class_tables.md)
- [Link to Lucid Chart](https://lucid.app/lucidchart/0aa9669d-b24f-49ac-94de-a36387722252/view)
- [Link to PDF Version of Lucid Chart](./ULM-Library.pdf)
