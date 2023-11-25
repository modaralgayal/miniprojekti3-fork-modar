from app import app
from flask import redirect, request, render_template
import book

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
            book.add_book(title, author, year, publisher, url)
            return redirect("/")

        if request.method == "GET":
            #users.check_csrf_token()
            books = book.get_books()
            articles = book.get_articles()
            if books == []:
                return redirect("/")
            return render_template("book.html", books=books, articles=articles)

    except Exception as error:
        return error_message(error, request, "/book", "/")

@app.route("/article", methods=["post", "get"])
def handle_article():
    try:
        if request.method == "POST":
            #users.check_csrf()
            title = request.form["title"]
            author = request.form["author"]
            year = request.form["year"]
            publisher = request.form["publisher"]
            url = request.form["url"]
            book.add_article(title, author, year, publisher, url)
            return redirect("/")

        if request.method == "GET":
            #users.check_csrf_token()
            articles = book.get_articles()
            if articles == []:
                return redirect("/")
            return render_template("book.html", articles=articles)

    except Exception as error:
        return error_message(error, request, "/article", "/")


