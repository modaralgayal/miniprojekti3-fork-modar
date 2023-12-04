from flask import Flask
from flask_bootstrap import Bootstrap
from os import getenv
from db import db
from os import getenv
from flask import Flask

app = Flask(__name__)

if getenv("production") == "test":
    db_address = "postgresql:///testi"
# elif getenv("production") == "test2":
#     db_address = "postgresql://test:test@localhost:5432"
else:
    db_address = getenv("DATABASE_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = db_address

app.secret_key = getenv("SECRET_KEY")

Bootstrap(app)
db.init_app(app)
app.app_context().push()

import routes
