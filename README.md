# os-backend

Backend for OnlyStreams created using the [Django framework](https://www.djangoproject.com/).

## Requirements

You'll notice that there are two requirements files:

- *requirements.txt* - list of hand-picked requirements
- *requirements.lock.txt* - list of all the requirements (hand-picked + their dependencies)

Install and freeze to *requirements.lock.txt* and update *requirements.txt* accordingly.

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