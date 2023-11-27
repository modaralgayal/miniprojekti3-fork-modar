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
    b_url TEXT
);

CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    a_year INTEGER,
    journal TEXT,
    a_url TEXT
);

CREATE TABLE inproceedings (
    inproceeding_id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    i_year INTEGER,
    i_url TEXT
);