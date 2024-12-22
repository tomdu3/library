# Library Record System - UML Class Diagram

```plaintext
+-----------------+
|     Book        |
+-----------------+
| - book_id       |
| - title         |
| - author        |
| - year          |
| - publisher     |
| - copies        |
| - available_copies |
| - publication_date |
+-----------------+
| + set_title()   |
| + get_title()   |
| + set_author()  |
| + get_author()  |
| + set_year()    |
| + get_year()    |
| + set_publisher() |
| + get_publisher() |
| + set_copies()  |
| + get_copies()  |
| + get_available_copies() |
+-----------------+

+-----------------+
|   BookList      |
+-----------------+
| - books         |
+-----------------+
| + add_book()    |
| + search_book() |
| + remove_book() |
| + total_books() |
+-----------------+

+-----------------+
|     User        |
+-----------------+
| - username      |
| - firstname     |
| - surname       |
| - house_number  |
| - street_name   |
| - postcode      |
| - email         |
| - dob           |
+-----------------+
| + get_username()|
| + get_firstname() |
| + set_firstname() |
+-----------------+

+-----------------+
|   UserList      |
+-----------------+
| - users         |
+-----------------+
| + add_user()    |
| + remove_user() |
| + count_users() |
+-----------------+

+-----------------+
|     Loan        |
+-----------------+
| - loans         |
+-----------------+
| + borrow_book() |
| + return_book() |
| + user_books_count() |
+-----------------+

```

# Library Record System - UML Class Diagram

### Book

| Attribute        | Type     | Description                          |
| ---------------- | -------- | ------------------------------------ |
| book_id          | int      | Randomly generated book ID           |
| title            | str      | Title of the book                    |
| author           | str      | Author of the book                   |
| year             | int      | Year of publication                  |
| publisher        | str      | Publisher of the book                |
| copies           | int      | Total number of copies               |
| available_copies | int      | Number of copies currently available |
| publication_date | str/date | Publication date of the book         |

| Method                 | Description                        |
| ---------------------- | ---------------------------------- |
| set_title()            | Set the title of the book          |
| get_title()            | Get the title of the book          |
| set_author()           | Set the author of the book         |
| get_author()           | Get the author of the book         |
| set_year()             | Set the publication year           |
| get_year()             | Get the publication year           |
| set_publisher()        | Set the publisher of the book      |
| get_publisher()        | Get the publisher of the book      |
| set_copies()           | Set the total number of copies     |
| get_copies()           | Get the total number of copies     |
| get_available_copies() | Get the number of available copies |

---

### BookList

| Attribute | Type | Description                  |
| --------- | ---- | ---------------------------- |
| books     | dict | A dictionary of book objects |

| Method        | Description                               |
| ------------- | ----------------------------------------- |
| add_book()    | Add a book to the collection              |
| search_book() | Search for a book by title, author, etc.  |
| remove_book() | Remove a book from the collection         |
| total_books() | Get the total number of books in the list |

---

### User

| Attribute    | Type     | Description                    |
| ------------ | -------- | ------------------------------ |
| username     | str      | Unique identifier for the user |
| firstname    | str      | User's first name              |
| surname      | str      | User's last name               |
| house_number | int      | User's house number            |
| street_name  | str      | Name of the user's street      |
| postcode     | str      | User's postal code             |
| email        | str      | User's email address           |
| dob          | str/date | User's date of birth           |

| Method          | Description                    |
| --------------- | ------------------------------ |
| get_username()  | Get the username of the user   |
| get_firstname() | Get the first name of the user |
| set_firstname() | Set the first name of the user |

---

### UserList

| Attribute | Type | Description                  |
| --------- | ---- | ---------------------------- |
| users     | dict | A dictionary of user objects |

| Method        | Description                               |
| ------------- | ----------------------------------------- |
| add_user()    | Add a user to the collection              |
| remove_user() | Remove a user by their first name         |
| count_users() | Get the total number of users in the list |

---

### Loan

| Attribute | Type | Description                  |
| --------- | ---- | ---------------------------- |
| loans     | dict | A dictionary of loaned books |

| Method             | Description                                 |
| ------------------ | ------------------------------------------- |
| borrow_book()      | Borrow a book for a user                    |
| return_book()      | Return a borrowed book                      |
| user_books_count() | Get the number of books a user has borrowed |
