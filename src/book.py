from flask import session
from sqlalchemy.sql import text
import app
from db import db


def add_book(title, author, year, publisher, url):
    sql = text(
        '''INSERT INTO books (title, author, b_year, publisher, b_url)
        VALUES (:title, :author, :year, :publisher, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "url": url
    })
    db.session.commit()


def get_books():
    sql = text(
        '''SELECT title, author, b_year, publisher, b_url FROM books''')
    result = db.session.execute(sql)
    books = result.fetchall()
    #print(books)
    return books


def add_article(title, author, year, publisher, url):
    sql = text(
        '''INSERT INTO articles (title, author, a_year, publisher, a_url)
        VALUES (:title, :author, :year, :publisher, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "publisher": publisher,
        "url": url
    })
    db.session.commit()


def get_articles():
    sql = text(
        '''SELECT title, author, a_year, publisher, a_url FROM articles''')
    result = db.session.execute(sql)
    articles = result.fetchall()
    #print(books)
    return articles
