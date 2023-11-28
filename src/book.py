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
        '''SELECT book_id, title, author, b_year, publisher, b_url FROM books''')
    result = db.session.execute(sql)
    books = result.fetchall()
    return books


def delete_book(id):
    sql = text(
        '''DELETE FROM books WHERE book_id=:id''')
    db.session.execute(sql, {"id": id})
    db.session.commit()
    return


def add_article(title, author, year, journal, url):
    sql = text(
        '''INSERT INTO articles (title, author, a_year, journal, a_url)
        VALUES (:title, :author, :year, :journal, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "journal": journal,
        "url": url
    })
    db.session.commit()


def get_articles():
    sql = text(
        '''SELECT article_id, title, author, a_year, journal, a_url FROM articles''')
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles


def delete_article(id):
    sql = text(
        '''DELETE FROM articles WHERE article_id=:id''')
    db.session.execute(sql, {"id": id})
    db.session.commit()
    return


def add_inproceeding(title, author, year, url):
    sql = text(
        '''INSERT INTO inproceedings (title, author, i_year, i_url)
        VALUES (:title, :author, :year, :url)''')
    db.session.execute(sql, {
        "title": title,
        "author": author,
        "year": year,
        "url": url
    })
    db.session.commit()


def get_inproceedings():
    sql = text(
        '''SELECT inproceeding_id, title, author, i_year, i_url FROM inproceedings''')
    result = db.session.execute(sql)
    inproceedings = result.fetchall()
    return inproceedings


def delete_inproceeding(id):
    sql = text(
        '''DELETE FROM inproceedings WHERE inproceeding_id=:id''')
    db.session.execute(sql, {"id": id})
    db.session.commit()
    return
