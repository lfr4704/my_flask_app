# my_flask_app

# Installation

# Setup

```sh
pipenv --python 3.7
```

```sh
pipenv install Flask Flask-SQLAlchemy Flask-Migrate
```

```sh
pipenv install python-dotenv requests basilica tweepy
```

```sh
pipenv install scikit-learn
```

Migrate the database:

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```

# Usage

```sh
FLASK_APP=web_app flask run
```

# deploying to Herok

```sh
heroku login
heroku create <name_of_app>
```

```sh
pipenv install gunicorn psycopg2-binary
```
