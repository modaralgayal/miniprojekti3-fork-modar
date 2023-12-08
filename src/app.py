from os import getenv
from flask import Flask
from flask_bootstrap import Bootstrap
from db import db



app = Flask(__name__)

if getenv("production") == "test":
    DB_ADDRESS = "postgresql://test:test@localhost:5432"
# if getenv("production") == "test":
#     DB_ADDRESS = "postgresql:///test"

else:
    DB_ADDRESS = getenv("DATABASE_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = DB_ADDRESS

app.secret_key = getenv("SECRET_KEY")

Bootstrap(app)
db.init_app(app)
app.app_context().push()

import routes
