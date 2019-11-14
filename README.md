[![Build Status](https://travis-ci.org/Paccy10/flask-ecommerce-api.svg?branch=master)](https://travis-ci.org/Paccy10/flask-ecommerce-api) [![Maintainability](https://api.codeclimate.com/v1/badges/df74b7e8f3bf97178a0f/maintainability)](https://codeclimate.com/github/Paccy10/flask-ecommerce-api/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/df74b7e8f3bf97178a0f/test_coverage)](https://codeclimate.com/github/Paccy10/flask-ecommerce-api/test_coverage)

# Arrows Online Shop API

Online shop API

## Installation and Setup

- Clone the repository

```
https://github.com/Paccy10/flask-ecommerce-api.git
```

- Create a virtual environment

```
pipenv shell
```

- Install dependencies

```
pipenv install
```

- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly:

```
DATABASE_URL = postgresql://YOUR_DATABASE_USER:YOUR_DATABASE_PASSWORD@YOUR_DATABASE_HOST/YOUR_DATABASE_NAME
TEST_DATABASE_URL = postgresql://YOUR_DATABASE_USER:YOUR_DATABASE_PASSWORD@YOUR_DATABASE_HOST/YOUR_TEST_DATABASE_NAME

SECRET_KEY = YOUR_SECRET_KEY

MAIL_SERVER = YOUR_MAIL_SERVER
MAIL_PORT = YOUR_MAIL_SERVER_PORT
MAIL_USE_TLS = True
MAIL_USERNAME = YOUR_MAIL_USERNAME
MAIL_PASSWORD = YOUR_MAIL_PASSWORD
```

- Apply migrations

```
flask db upgrade
```

- Should you make changes to the database models, run migrations as follows

  - Migrate database

  ```
  flask db migrate
  ```

  - Upgrade to the new structure

  ```
  flask db upgrade
  ```

- Run the application

```
flask run
```

# Running tests and generating report

```
pytest
```

To further view the lines not tested or covered if there is any, an `htmlcov` directory will be created, get the `index.html` file by entering the directory and view it in your browser.
