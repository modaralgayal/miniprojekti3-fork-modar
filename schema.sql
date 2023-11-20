-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     username TEXT UNIQUE,
--     password TEXT
-- );

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    b_year INTEGER,
    publisher TEXT,
    b_address TEXT
);