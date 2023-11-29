from app import app
from flask import redirect, request, render_template
import reference
from db import db


def error_message(error, req, route, link):
    print(f"The error is {route}({req.method}): {error}")
    user_error = f"({req.method}) in {route}: {type(error).__name__}"
    return render_template("error.html", message=user_error, link=link)

  
@app.route('/')
def welcome():
    return render_template('index.html')


@app.route("/book", methods=["post", "get"])
def handle_book():
    try:
        if request.method == "POST":
            #users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            publisher = request.form["publisher"]
            url = request.form["url"]
            reference.add_book(title, author, year, publisher, url, db)
            return render_template('index.html', 
                message=f"Added book {title} by {author} to database")

        if request.method == "GET":
            #users.check_csrf_token()
            books = reference.get_books(db)
            articles = reference.get_articles(db)
            inproceedings = reference.get_inproceedings(db)
            #if books == []:
                #return redirect("/")
            return render_template("book.html", books=books, articles=articles,
                                   inproceedings=inproceedings)

    except Exception as error:
        return error_message(error, request, "/book", "/")

      
@app.route("/article", methods=["post"])
def handle_article():
    try:
        if request.method == "POST":
            #users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            journal = request.form["journal"]
            url = request.form["url"]
            reference.add_article(title, author, year, journal, url,db)
            return render_template('index.html', 
                message=f"Added article {title} by {author} to database")

    except Exception as error:
        return error_message(error, request, "/article", "/")

      
@app.route("/inproceeding", methods=["post"])
def handle_inproceeding():
    try:
        if request.method == "POST":
            #users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            url = request.form["url"]
            reference.add_inproceeding(title, author, year, url,db)
            return render_template('index.html', 
                message=f"Added inproceeding {title} by {author} to database")

    except Exception as error:
        return error_message(error, request, "/inproceeding", "/")
