from flask import session
from sqlalchemy.sql import text
import app
from db import db


def add_book(title, author, year, publisher, address):
    sql = text(
        '''INSERT INTO books (title, author, b_year, publisher, b_address)
        VALUES (:title, :author, :year, :publisher, :address)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "address": address
    })
    db.session.commit()


def get_books():
    sql = text(
        '''SELECT title, author, b_year, publisher, b_address FROM books''')
    result = db.session.execute(sql)
    books = result.fetchall()
    #print(books)
    return books

