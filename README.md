# Django_postgresql_
1. Installing the required libraries:
pipenv install django
pipenv install djangorestframework
   
2. Create project database: django-admin startproject database .
python manage.py migrate
python manage.py runserver

3. And create app apidb: python manage.py startapp apidb
python manage.py migrate
python manage.py makemigrations apidb

4. We make the necessary changes to settings.py. 
Name App (apidb), rest_framework and database options (in our case it is postgresql)

5. Create superuser: python manage.py createsuperuser 
and update our application's admin.py file

6. Starting a local server: python manage.py runserver
