
# UML Class Diagram: Library Management System

## Classes

### Book
```
+----------------------------+
|           Book             |
+----------------------------+
| - used_ids: List[int]      |
+----------------------------+
| + __init__(...)            |
| + generate_book_id(): int  |
| + validate_inputs(...)     |
| + set_title(title: str)    |
| + get_title(): str         |
| + set_author(author: str)  |
| + get_author(): str        |
| + set_year(year: int)      |
| + get_year(): int          |
| + set_publisher(...)       |
| + get_publisher(): str     |
| + set_copies(copies: int)  |
| + get_copies(): int        |
| + get_available_copies(): int |
| + __str__(): str           |
+----------------------------+
```

### BookList
```
+----------------------------+
|         BookList           |
+----------------------------+
| - books: Dict[int, Book]   |
+----------------------------+
| + __init__()               |
| + add_book(book: Book)     |
| + search_book(**kwargs): Book |
| + remove_book(book_id: int) |
| + total_books: int (property) |
| + __str__(): str           |
+----------------------------+
```

### User
```
+----------------------------+
|           User             |
+----------------------------+
| - usernames: List[str]     |
+----------------------------+
| + __init__(...)            |
| + check_username(username: str) |
| + get_username(): str      |
| + get_firstname(): str     |
| + set_firstname(firstname: str) |
| + get_lastname(): str      |
| + set_lastname(lastname: str) |
| + get_address(): str       |
| + set_address(...)         |
| + validate_email(email: str) |
| + get_email(): str         |
| + set_email(email: str)    |
| + validate_dob(dob: str)   |
| + get_dob(): str           |
| + set_dob(dob: str)        |
| + __str__(): str           |
+----------------------------+
```

### UserList
```
+----------------------------+
|         UserList           |
+----------------------------+
| - users: Dict[str, User]   |
+----------------------------+
| + __init__()               |
| + add_user(user: User)     |
| + remove_user(firstname: str) |
| + count_users(): int       |
| + __str__(): str           |
+----------------------------+
```

### Loan
```
+----------------------------+
|           Loan             |
+----------------------------+
| - loans: Dict[str, List[Book]] |
+----------------------------+
| + __init__()               |
| + borrow_book(username: str, book: Book) |
| + return_book(username: str, book: Book) |
| + user_books_count(username: str): int |
| + __str__(): str           |
+----------------------------+
```

### LibraryDashboard
```
+----------------------------+
|    LibraryDashboard        |
+----------------------------+
| - book_list: BookList      |
| - user_list: UserList      |
| - loan: Loan               |
+----------------------------+
| + __init__()               |
| + display_menu()           |
| + manage_books()           |
| + manage_users()           |
| + manage_loans()           |
| + add_book()               |
| + search_book()            |
| + remove_book()            |
| + view_all_books()         |
| + add_user()               |
| + remove_user()            |
| + view_all_users()         |
| + borrow_book()            |
| + return_book()            |
| + view_user_loans()        |
| + run()                    |
+----------------------------+
```

## Relationships

- **LibraryDashboard** uses:
  - `BookList`
  - `UserList`
  - `Loan`

- **BookList** contains:
  - `Book`

- **Loan** references:
  - `Book`
  - `User`

- **UserList** contains:
  - `User`
