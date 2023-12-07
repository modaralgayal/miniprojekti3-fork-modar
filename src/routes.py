from app import app
from flask import redirect, request, render_template, session, send_file
import reference
from db import db


def error_message(error, req, route, link):
    print(f"The error is {route}({req.method}): {error}")
    user_error = f"({req.method}) in {route}: {type(error).__name__}"
    return render_template("error.html", message=user_error, link=link)


@app.route('/')
def index():
    if 'message' in session and 'message_type' in session:
        message = session['message']
        message_type = session['message_type']
        del session['message']
        del session['message_type']
    else:
        message = None
        message_type = None
    return render_template('index.html', message=message, message_type=message_type)


@app.route('/reference_forms')
def reference_forms():
    return render_template('add_references.html')


@app.route("/reference_lists")
def reference_lists():
    try:
        # users.check_csrf_token()
        books = reference.get_books(db)
        articles = reference.get_articles(db)
        inproceedings = reference.get_inproceedings(db)
        return render_template(
            "list_references.html",
            books=books,
            articles=articles,
            inproceedings=inproceedings)
    except Exception as error:
        return error_message(error, request, "/", "/")


@app.route("/book", methods=["post"])
def handle_book():
    try:
        if request.method == "POST":
            # users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            publisher = request.form["publisher"]
            url = request.form["url"]
            reference.add_book(title, author, year, publisher, url, db)
            session['message'] = f"Added book {title} by {author} to database"
            session['message_type'] = 'success'
            return redirect('/')
    except Exception as error:
        session['message'] = f"Error when adding book"
        session['message_type'] = 'danger'
        return redirect('/')


@app.route("/article", methods=["post"])
def handle_article():
    try:
        if request.method == "POST":
            # users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            journal = request.form["journal"]
            url = request.form["url"]
            reference.add_article(title, author, year, journal, url, db)
            session['message'] = f"Added article {title} by {author} to database"
            session['message_type'] = 'success'
            return redirect('/')
    except Exception as error:
        session['message'] = f"Error when adding article"
        session['message_type'] = 'danger'
        return redirect('/')


@app.route("/inproceeding", methods=["post"])
def handle_inproceeding():
    try:
        if request.method == "POST":
            # users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            url = request.form["url"]
            reference.add_inproceeding(title, author, year, url, db)
            session['message'] = f"Added inproceeding {title} by {author} to database"
            session['message_type'] = 'success'
            return redirect('/')
    except Exception as error:
        session['message'] = f"Error when adding inproceeding"
        session['message_type'] = 'danger'
        return redirect('/')


@app.route("/bibtex-file", methods=["get"])
def bibtex_file():
    try:
        data = reference.get_data(db)
        reference.write_bibtex_file(data)
        path = 'viitteet.bib'
        return send_file(path, as_attachment=True)
    except Exception as error:
        session['message'] = f"Error when downloading Bibtex.file"
        session['message_type'] = 'danger'
        return redirect('/')


@app.route("/delete_reference", methods=["post"])
def delete_reference():
    reference_id = request.form["reference_id"]
    reference_type = request.form["reference_type"]

    if reference_type == "book":
        reference.delete_book(reference_id, db)
    elif reference_type == "article":
        reference.delete_article(reference_id, db)
    elif reference_type == "inproceeding":
        reference.delete_inproceeding(reference_id, db)
    else:
        return redirect('/')

    session['message'] = f"Deleted {reference_type} with id={reference_id} from database"
    session['message_type'] = 'danger'
    return redirect('/')
