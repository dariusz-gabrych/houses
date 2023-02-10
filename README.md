# houses

# How to run:

1. Prepare .env file in the root of the project, (you can use .env.sample as a base).

2. Run command `docker-compose up` to start application.

3. Run command `docker-compose run web python manage.py migrate` in new terminal to apply migrations to database.

4. If you change database structure, e.g. by adding new column, or changing some properties in the table, please run command `docker-compose run web python manage.py makemigrations` to reflect your changes in migration, and then run command `docker-compose run web migrate` if you want to apply them.

5. Go to http://localhost:8000
