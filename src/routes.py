from app import app
from flask import redirect, request, render_template, session
import reference
from db import db


def error_message(error, req, route, link):
    print(f"The error is {route}({req.method}): {error}")
    user_error = f"({req.method}) in {route}: {type(error).__name__}"
    return render_template("error.html", message=user_error, link=link)


@app.route('/')
def index():
    if 'message' in session:
        message = session['message']
        del session['message']
    else:
        message = None
    return render_template('index.html', message=message)


@app.route('/reference_forms')
def reference_forms():
    return render_template('add_references.html')


@app.route("/reference_lists")
def reference_lists():
    try:
        #users.check_csrf_token()
        books = reference.get_books(db)
        articles = reference.get_articles(db)
        inproceedings = reference.get_inproceedings(db)
        return render_template("list_references.html", books=books, articles=articles,
                               inproceedings=inproceedings)

    except Exception as error:
        return error_message(error, request, "/", "/")


@app.route("/book", methods=["post"])
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
            session['message'] = f"Added book {title} by {author} to database"
            return redirect('/')
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
            reference.add_article(title, author, year, journal, url, db)
            session['message'] = f"Added article {title} by {author} to database"
            return redirect('/')

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
            reference.add_inproceeding(title, author, year, url, db)
            session['message'] = f"Added inproceeding {title} by {author} to database"
            return redirect('/')

    except Exception as error:
        return error_message(error, request, "/inproceeding", "/")


@app.route("/delete_book", methods=["post"])
def delete_book():
    book_id = request.form["book_id"]
    reference.delete_book(book_id, db)
    session['message'] = f"Deleted book (id: {book_id}) from database"
    return redirect('/')


@app.route("/delete_article", methods=["post"])
def delete_article():
    article_id = request.form["article_id"]
    reference.delete_article(article_id, db)
    session['message'] = f"Deleted article (id: {article_id}) from database"
    return redirect('/')


@app.route("/delete_inproceeding", methods=["post"])
def delete_inproceeding():
    inproceeding_id = request.form["inproceeding_id"]
    reference.delete_inproceeding(inproceeding_id, db)
    session['message'] = f"Deleted inproceeding (id: {inproceeding_id}) from database"
    return redirect('/')
