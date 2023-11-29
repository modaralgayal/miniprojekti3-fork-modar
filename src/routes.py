from app import app
from flask import redirect, request, render_template
import book


def error_message(error, req, route, link):
    print(f"The error is {route}({req.method}): {error}")
    user_error = f"({req.method}) in {route}: {type(error).__name__}"
    return render_template("error.html", message=user_error, link=link)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reference_forms')
def reference_forms():
    return render_template('add_references.html')


@app.route("/reference_lists")
def reference_lists():
    try:
        #users.check_csrf_token()
        books = book.get_books()
        articles = book.get_articles()
        inproceedings = book.get_inproceedings()
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
            book.add_book(title, author, year, publisher, url)
            return redirect("/")
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
            book.add_article(title, author, year, journal, url)
            return redirect("/")

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
            book.add_inproceeding(title, author, year, url)
            return redirect("/")

    except Exception as error:
        return error_message(error, request, "/inproceeding", "/")


@app.route("/delete_book", methods=["post"])
def delete_book():
    book.delete_book(request.form["book_id"])
    return redirect("/")
