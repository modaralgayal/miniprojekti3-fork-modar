# miniprojekti3

## Setting up and running:

Get the source code, clone the project.

Create .env-file to project root with following contents
(your_db_name and your_secret_key can be chosen freely at this point):
>DATABASE_URL="postgresql:///your_db_name"
> 
>SECRET_KEY="your_secret_key"

Activate virtual environment and install project dependencies:

>$ python3 -m venv venv

>$ source venv/bin/activate

>$ pip install -r ./requirements.txt

Run the Flask application:

>$ flask run

Open the flask-webpage with your browser (Usual URL is http://127.0.0.1:5000).
