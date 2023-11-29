# miniprojekti3
![GHA workflow badge](https://github.com/ValioEilax/miniprojekti3/workflows/CI/badge.svg)

## Description:

Miniproject-exercise of group number 3 for a course "TKT20006 - Ohjelmistotuotanto" at University of Helsinki in fall 2023.

## Setting up the project:

Get the source code, clone the project.

The project uses PostgreSQL. It can be installed from /src/documents/resources/local-pg-master-folder.
It contains using the script "pg-install.sh" and instructions in its own "README.md".

The ".env"-file should NOT be added to git.

Create a file named ".env" to "src"-folder with following contents
(your_db_name and your_secret_key can be chosen freely at this point):
>DATABASE_URL="postgresql:///your_db_name"
>SECRET_KEY="your_secret_key"

Activate virtual environment and install project dependencies with Poetry:
> poetry install --no-root


Define database tables from schema.sql in "src"-folder:
>$ psql (database_name) < schema.sql

## Running the project:

Start the virtual environment and shell:
> poetry shell

Go to "src"-folder:
> cd src

Run the Flask application:
>flask run

Open the flask-webpage with your browser (Usual URL is http://127.0.0.1:5000).

Flask application can be stopped in terminal py pressing:
> ctrl+c

Shell can be exited with a command:
> exit

## Documentation
- [Työaikakirjanpito](https://docs.google.com/spreadsheets/d/1tvDweyWHiYNj0rdVt22RT_IMBiqbW4Og1WdRkrPofMc/edit?usp=sharing)
- [Definition of Done](https://github.com/ValioEilax/miniprojekti3/blob/main/src/documents/dod.md)
- [Product & Sprint Backlogs](https://github.com/users/ValioEilax/projects/1/views/1?layout=table)
