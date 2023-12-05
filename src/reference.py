from flask import session
from sqlalchemy.sql import text
#import app
#from db import db


def add_book(title, author, year, publisher, url, db):
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


def get_books(db):
    sql = text(
        '''SELECT book_id, title, author, b_year, publisher, b_url FROM books''')
    result = db.session.execute(sql)
    books = result.fetchall()
    return books


def delete_book(book_id, db):
    sql = text(
        '''DELETE FROM books WHERE book_id=:id''')
    db.session.execute(sql, {"id": book_id})
    db.session.commit()
    return


def add_article(title, author, year, journal, url, db):
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


def get_articles(db):
    sql = text(
        '''SELECT article_id, title, author, a_year, journal, a_url FROM articles''')
    result = db.session.execute(sql)
    articles = result.fetchall()
    return articles


def delete_article(article_id, db):
    sql = text(
        '''DELETE FROM articles WHERE article_id=:id''')
    db.session.execute(sql, {"id": article_id})
    db.session.commit()
    return



def add_inproceeding(title, author, year, url, db):
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


def get_inproceedings(db):
    sql = text(
        '''SELECT inproceeding_id, title, author, i_year, i_url FROM inproceedings''')
    result = db.session.execute(sql)
    inproceedings = result.fetchall()
    return inproceedings


def delete_inproceeding(inproceeding_id, db):
    sql = text(
        '''DELETE FROM inproceedings WHERE inproceeding_id=:id''')
    db.session.execute(sql, {"id": inproceeding_id})
    db.session.commit()
    return


def get_data(db):
    result = []
    print("moi")
    books = get_books(db)
    articles = get_articles(db)
    inproceedings = get_inproceedings(db)
    result.append(books)
    result.append(articles)
    result.append(inproceedings)
    print(books)
    print(articles)
    print(inproceedings)
    print(result)
    return result

  
def template_books(entry):
    result='@book{'+entry[1]+str(entry[3])+',\n title = "'+entry[1]+'",\n author = "'+entry[2]+'",\n year = '+str(entry[3])+',\n publisher = "'+entry[4]+'",\n url = "'+entry[5]+'",\n}\n\n'
    print(result)
    return result

  
def template_articles(entry):
    result='@article{'+entry[1]+str(entry[3])+',\n title = "'+entry[1]+'",\n author = "'+entry[2]+'",\n year = '+str(entry[3])+',\n journal = "'+entry[4]+'",\n url = "'+entry[5]+'",\n}\n\n'
    print(result)
    return result

  
def template_inproceedings(entry):
    result='@inproceedings{'+entry[1]+str(entry[3])+',\n title = "'+entry[1]+'",\n author = "'+entry[2]+'",\n year = '+str(entry[3])+',\n url = "'+entry[4]+'",\n}\n\n'
    print(result)
    return result

  
def write_bibtex_file(data):
    with open('viitteet.bib', 'w') as file:

        for entry in data[0]:
            print("moi1")
            bibtex_entry = template_books(entry)
            file.write(bibtex_entry)

        for entry in data[1]:
            print("moi2")
            bibtex_entry = template_articles(entry)
            file.write(bibtex_entry)

        for entry in data[2]:
            print("moi3")
            bibtex_entry = template_inproceedings(entry)
            file.write(bibtex_entry)


def initialize_test_database(db):
    schemafile = open("delschema.sql", "r")
    sql = text(schemafile.read())
    schemafile.close()
    db.session.execute(sql)
    schemafile2 = open("schema.sql", "r")
    sql = text(schemafile2.read())
    schemafile2.close()
    db.session.execute(sql)
    db.session.commit()
