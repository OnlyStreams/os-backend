# os-backend

Backend for OnlyStreams created using the [Django framework](https://www.djangoproject.com/).

## Requirements

You'll notice that there are two requirements files:

- *requirements.txt* - list of hand-picked requirements
- *requirements.lock.txt* - list of all the requirements (hand-picked + their dependencies)

Install and freeze to *requirements.lock.txt* and update *requirements.txt* accordingly.

## Development setup

1. Create a new virtual environment.
2. Install the packages using `pip install -r requirements.lock.txt`.
3. Create a new `.env` file and put the following inside:
    ```
   # Django secret key used for hashing (do not share!)
   # You can generate it by using the following service: https://djecrety.ir/
   SECRET_KEY=<generated_django_secret_key>
   
   # Can be generated the same way as Django's SECRET_KEY
   JWT_SECRET_KEY=<generated_jwt_secret_key>
   
   DEBUG=true
   ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
   CORS_ALLOWED_ORIGINS=http://localhost:3000 http://127.0.0.1:3000
   TIMEZONE=Europe/Berlin
   
   SECURE_HSTS=false
   # dev=30, prod=2592000, only taken into account if SECURE_HSTS is enabled
   SECURE_HSTS_SECONDS=30
   
   DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
   DATABASE_NAME=<db_name>
   DATABASE_USER=<db_user>
   DATABASE_PASSWORD=<db_password>
   DATABASE_HOST=<db_host>
   DATABASE_PORT=<db_port>
   
   API_NAME=os-backend
   API_DESCRIPTION=there are no accidents
   API_URL=http://localhost:8000/api/
   API_VERSION=1.0
   API_AUTHORS=Nik Tomazic (duplxey)
   
   STATIC_ROOT=/var/www/staticfiles/
   MEDIA_ROOT=/var/www/mediafiles/
    ```
4. Get [PostgreSQL](https://www.postgresql.org/) up and running (either with Docker or by [installing it locally](https://www.postgresql.org/download/)).
    ```sh
    $ docker run --name <name>-postgres -p 5432:5432 \
        -e POSTGRES_USER=<db_user> -e POSTGRES_PASSWORD=<db_password> \
        -e POSTGRES_DB=<db_name> -d postgres
    ```
5. Make migrations `python manage.py makemigrations`.
6. Migrate the database using `python manage.py migrate`.
7. Run the server using `python manage.py runserver`.

> If you're running Windows, you'll also have to install `psycopg2` using pip.

## Testing

Before a new release, you should always check if all the tests execute successfully. 

To run all the tests:

 ```
$ python manage.py test -v 2
 ```

To run specific tests:

 ```
# Run all the tests in the animals.tests module
$ python ./manage.py test animals.tests -v 2

# Run all the tests found within the 'animals' package
$ python ./manage.py test animals -v 2

# Run just one test case
$ python ./manage.py test animals.tests.AnimalTestCase -v 2

# Run just one test method
$ python ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak -v 2
 ```

## Code linting & formatting

Code formatting and linting is done via:

- [black](https://black.readthedocs.io/en/stable/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [isort](https://pycqa.github.io/isort/)

To setup Git hooks to automatically lint and format your code:

1. Install the Git hook via [pre-commit](https://pre-commit.com/):
   ```
   $ pre-commit install
   ```
2. Test the hook:
   ```
   $ pre-commit run --all-files
   ```
3. Voila! All the linters and formatters are going to get called before you commit.