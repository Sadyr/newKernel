DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS jenre_books;
DROP TABLE IF EXISTS statuses;
DROP TABLE IF EXISTS authors;



CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE jenre_books (
    jenre_book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    jenre_book_name TEXT NOT NULL
);


CREATE TABLE statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT NOT NULL
);

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_title TEXT UNIQUE NOT NULL,
    book_author_id INTEGER NOT NULL,
    book_description TEXT NOT NULL,
    book_jenre_id INTEGER NOT NULL,
    book_status_id INTEGER NOT NULL,
    FOREIGN KEY (book_author_id) REFERENCES authors (author_id),
    FOREIGN KEY (book_jenre_id) REFERENCES jenre_books (jenre_book_id),
    FOREIGN KEY (book_status_id) REFERENCES statuses (status_id)

);

CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT UNIQUE NOT NULL
);